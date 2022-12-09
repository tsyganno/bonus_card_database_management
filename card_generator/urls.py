from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from card_generator.views import MainView, CardDetailView


urlpatterns = [
    path('', MainView.as_view(), name='index'),
    path('<slug>/', CardDetailView.as_view(), name='card_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
