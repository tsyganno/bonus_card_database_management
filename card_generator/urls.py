from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from card_generator.views import MainView, CardDetailView, SearchResultsView


urlpatterns = [
    path('', MainView.as_view(), name='index'),
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('<int:pk>/', CardDetailView.as_view(), name='card_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
