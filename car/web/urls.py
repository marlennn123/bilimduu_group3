
from django.urls import path
from .views import CarView, CarBetView
urlpatterns = [
    path('car/', CarView.as_view({'get': 'list', 'post': 'create', 'put': 'update', 'delete': 'destroy'}, name='product_list')),
    path('carbat/', CarBetView.as_view({'get': 'list', 'post': 'create', 'put': 'update', 'delete': 'destroy'}, name='carbet_list')),
]
