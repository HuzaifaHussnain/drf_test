from django.shortcuts import render
from rest_framework import generics
from .serializers import UserSerializer
from .models import User


class UserListUpdateView(generics.ListAPIView, generics.UpdateAPIView):
	""" View for listing all the user and updating the User information of the current user """
	serializer_class = UserSerializer
	queryset = User.objects.all()

	def get_object(self):
		return self.request.user
