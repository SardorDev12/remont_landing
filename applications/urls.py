# app_1/urls.py
from django.urls import path
from .views import ApplicationCreate, ApplicationListCreateView

urlpatterns = [
    path('', ApplicationListCreateView.as_view(), name='application-list-create'),
    path('create/', ApplicationCreate.as_view(), name='application-create'),
]
