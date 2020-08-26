from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
	""" Serializer for Post model """

	user = serializers.CharField(source='user.get_full_name', read_only=True)
	class Meta:
		model = Post
		fields = ['id', 'user', 'content']
		read_only_fields = ['user']
		