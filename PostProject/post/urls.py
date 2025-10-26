from django.urls import path
from .views import HomePrev

urlpatterns = [
    path('', HomePrev.as_view(), name = 'home'),
]
