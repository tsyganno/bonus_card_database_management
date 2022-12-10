from django.shortcuts import render, reverse
from django.views import View
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django import http
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin

from card_generator.models import CardGenerator, Usage
from card_generator.forms import CardForm


class MainView(View):

    def get(self, request, *args, **kwargs):
        cards = CardGenerator.objects.all()
        paginator = Paginator(cards, 6)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'card_generator/home.html', context={'page_obj': page_obj})


class CardDetailView(UpdateView):
    model = CardGenerator
    form_class = CardForm

    def get_success_url(self):
        card = get_object_or_404(CardGenerator, id=self.kwargs['pk'])
        return reverse('card_detail', kwargs={"pk": card.pk})

    def get(self, request, *args, **kwargs):
        card = get_object_or_404(CardGenerator, id=self.kwargs['pk'])
        usage = Usage.objects.filter(card_generator__id=card.pk)
        return render(request, 'card_generator/card_detail.html', context={'card': card, 'usage': usage, 'form': CardForm()})


class SearchResultsView(View):

    def get(self, request, *args, **kwargs):
        query = self.request.GET.get('q')
        results = ""
        if query:
            results = CardGenerator.objects.filter(
                Q(card_series__icontains=query) |
                Q(number_card__icontains=query) |
                Q(card_issue_date__icontains=query) |
                Q(end_date_of_card_activity__icontains=query) |
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


class CardDeleteView(DeleteView):
    template_name = 'card_generator/card_detail.html'
    model = CardGenerator

    def delete(self, *args, **kwargs):
        self.object.objects.get(id=self.kwargs['pk'])
        return super(CardDeleteView, self).delete(*args, **kwargs)

    def get_success_url(self):
        return reverse('index')
