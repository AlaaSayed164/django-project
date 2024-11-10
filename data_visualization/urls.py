from django.urls import path
from .views import chart_view

urlpatterns = [
    path('', chart_view, name='chart'),
]
