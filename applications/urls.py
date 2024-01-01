# app_1/urls.py
from django.urls import path
from .views import ApplicationCreate, ApplicationListCreateView

urlpatterns = [
    path('application/', ApplicationListCreateView.as_view(), name='application-list-create'),
    path('application/create/', ApplicationCreate.as_view(), name='application-create'),
]
