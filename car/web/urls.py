
from django.urls import path
from .views import CarView
urlpatterns = [
    path('car/', CarView.as_view({'get': 'list'}))
]
