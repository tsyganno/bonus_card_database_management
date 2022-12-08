from django.urls import path

from card_generator.views import MainView


urlpatterns = [
    path('', MainView.as_view(), name='index'),
]
