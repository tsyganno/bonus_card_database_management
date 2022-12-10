from django.shortcuts import render
from django.views import View
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from django.db.models import Q

from card_generator.models import CardGenerator, Usage


class MainView(View):

    def get(self, request, *args, **kwargs):
        cards = CardGenerator.objects.all()
        paginator = Paginator(cards, 6)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'card_generator/home.html', context={'page_obj': page_obj})


class CardDetailView(View):

    def get(self, request, *args, **kwargs):
        card = get_object_or_404(CardGenerator, id=self.kwargs['pk'])
        usage = Usage.objects.filter(card_generator__id=card.pk)
        return render(request, 'card_generator/card_detail.html', context={'card': card, 'usage': usage})


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



