from django.urls import path
from .views import CommentCreate,CommentListAPIView

urlpatterns = [
    path('', CommentListAPIView.as_view(), name='application-list-create'),
    path('create/', CommentCreate.as_view(), name='application-create'),
]