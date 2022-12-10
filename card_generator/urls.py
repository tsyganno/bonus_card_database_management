from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from card_generator.views import MainView, CardDetailView, SearchResultsView, CardDeleteView


urlpatterns = [
    path('', MainView.as_view(), name='index'),
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('<int:pk>/', CardDetailView.as_view(), name='card_detail'),
    path('delete/<int:pk>/', CardDeleteView.as_view(), name='delete_card'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
