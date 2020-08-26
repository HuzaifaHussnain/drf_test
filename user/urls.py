from django.urls import path
from .views import UserListUpdateView


urlpatterns = [
    path('', UserListUpdateView.as_view()),
]
