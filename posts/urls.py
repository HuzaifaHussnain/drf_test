from django.urls import path
from .views import PostListCreateView, PostUpdateView

urlpatterns = [
    path('', PostListCreateView.as_view()),
    path('update/<int:pk>', PostUpdateView.as_view())
]
