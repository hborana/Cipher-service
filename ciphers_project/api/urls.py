from django.urls import path
from .views import greeting
from .views import encode
urlpatterns = [
    path('', greeting),
    path('caesar/<str:plain_text>/<int:shift>/', encode)
]
