# myproject/urls.py

from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.welome_page, name='welome_page'),
    path('', views.welome_page, name='welome_page'),
    path('predict/', views.predict_page, name='predict_page'),
]
