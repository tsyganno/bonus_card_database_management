from django.shortcuts import render
from django.views import View
from django.core.paginator import Paginator

from card_generator.models import CardGenerator


class MainView(View):

    def get(self, request, *args, **kwargs):
        cards = CardGenerator.objects.all()
        paginator = Paginator(cards, 6)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'card_generator/home.html', context={'page_obj': page_obj})
