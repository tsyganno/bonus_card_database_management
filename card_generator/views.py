from django.shortcuts import render
from django.views import View
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404

from card_generator.models import CardGenerator, Usage


class MainView(View):

    def get(self, request, *args, **kwargs):
        cards = CardGenerator.objects.all()
        paginator = Paginator(cards, 6)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'card_generator/home.html', context={'page_obj': page_obj})


class CardDetailView(View):

    def get(self, request, slug, *args, **kwargs):
        card = get_object_or_404(CardGenerator, card_series=slug)
        usage = Usage.objects.filter(card_generator__id=card.pk)
        return render(request, 'card_generator/card_detail.html', context={'card': card, 'usage': usage})
