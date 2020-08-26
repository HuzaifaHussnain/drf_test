from django.shortcuts import render
from .serializers import PostSerializer
from .models import Post
from rest_framework import generics


class PostListCreateView(generics.ListCreateAPIView):
	""" View for listing and creating posts"""

	serializer_class = PostSerializer
	queryset = Post.objects.all()

	def perform_create(self, serializer):
		serializer.save(user=self.request.user)


class PostUpdateView(generics.UpdateAPIView):
	""" view for updating the Post """
	serializer_class = PostSerializer

	def get_queryset(self):
		""" Filtering queryset to show only the user's posts """
		return Post.objects.filter(user=self.request.user)