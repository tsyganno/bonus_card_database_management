from datetime import datetime, timedelta

from django.shortcuts import render, reverse
from django.views import View
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.views.generic import UpdateView, DeleteView
from django.views.generic.edit import CreateView
from django.utils import timezone

from card_generator.models import CardGenerator, Usage
from card_generator.forms import CardForm, CreateCardForm


months = {'янв': '01', 'фев': '02', 'март': '03', 'апр': '04', 'ма': '05', 'июн': '06', 'июл': '07', 'авг': '08', 'сент': '09', 'окт': '10', 'нояб': '11', 'дек': '12'}


class MainView(View):

    def get(self, request, *args, **kwargs):
        cards = CardGenerator.objects.all()
        paginator = Paginator(cards, 6)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'card_generator/home.html', context={
            'page_obj': page_obj
        })


class CardDetailView(UpdateView):
    model = CardGenerator
    form_class = CardForm

    def get_success_url(self):
        card = get_object_or_404(CardGenerator, id=self.kwargs['pk'])
        return reverse('card_detail', kwargs={
            "pk": card.pk
        })

    def get(self, request, *args, **kwargs):
        card = get_object_or_404(CardGenerator, id=self.kwargs['pk'])
        usage = Usage.objects.filter(card_generator__id=card.pk)
        time_now = timezone.now()
        if card.end_date_of_card_activity < time_now:
            card.card_status = 'Не активирована'
            card.save()
            overdue = 'Просрочена'
            return render(request, 'card_generator/card_detail.html', context={
                'card': card,
                'usage': usage,
                'overdue': overdue
            })
        activity_end_date = 'больше 12 месяцев'
        result_date_one_year = card.end_date_of_card_activity - timedelta(days=365)
        result_date_six_month = card.end_date_of_card_activity - timedelta(days=183)
        result_date_one_month = card.end_date_of_card_activity - timedelta(days=31)
        if result_date_one_month <= time_now < result_date_one_year:
            activity_end_date = '12 месяцев'
        elif result_date_six_month <= time_now < result_date_one_month:
            activity_end_date = '6 месяцев'
        elif result_date_one_month <= time_now < card.end_date_of_card_activity:
            activity_end_date = '1 месяц'
        return render(request, 'card_generator/card_detail.html', context={
            'activity_end_date': activity_end_date,
            'card': card,
            'usage': usage,
            'form': CardForm()
        })


class SearchResultsView(View):

    def get(self, request, *args, **kwargs):
        query = self.request.GET.get('q')
        results = ""
        query_date = ''
        if query and 'г.' in query:
            try:
                array_date = query[: query.find('г.')].strip().split()
                for key in months.keys():
                    if key in array_date[1]:
                        query_date = f'{array_date[2]} {months[key]} {array_date[0]}'
                results = CardGenerator.objects.filter(
                    Q(card_issue_date__startswith=datetime.strptime(query_date, '%Y %m %d').date()) |
                    Q(end_date_of_card_activity__startswith=datetime.strptime(query_date, '%Y %m %d').date())
                )
            except:
                pass
        elif query:
            results = CardGenerator.objects.filter(
                Q(card_series__icontains=query) |
                Q(number_card__icontains=query) |
                Q(card_status__icontains=query)
            )
        paginator = Paginator(results, 6)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'card_generator/search.html', context={
            'title': 'Поиск',
            'results': page_obj,
            'count': paginator.count
        })


class CardCreateView(CreateView):
    template_name = 'card_generator/create_card.html'
    model = CardGenerator
    form_class = CreateCardForm

    def get_success_url(self):
        return reverse('index')


class CardDeleteView(DeleteView):
    template_name = 'card_generator/card_detail.html'
    model = CardGenerator

    def delete(self, *args, **kwargs):
        self.object.objects.get(id=self.kwargs['pk'])
        return super(CardDeleteView, self).delete(*args, **kwargs)

    def get_success_url(self):
        return reverse('index')
