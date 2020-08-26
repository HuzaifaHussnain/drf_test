from .models import User, UserProfile
from rest_framework import serializers



class UserProfileSerializer(serializers.ModelSerializer):
	class Meta:
		model = UserProfile
		fields = ['bio', 'profile_pic']


class UserSerializer(serializers.ModelSerializer):
	""" Serializer for User model """
	profile = UserProfileSerializer()
	full_name = serializers.SerializerMethodField()
	
	class Meta:
		model = User
		fields = ['email', 'full_name', 'first_name', 'last_name', 'profile']
		extra_kwargs = {
            'email': {'read_only': True},
            'first_name': {'write_only': True},	# so that you can update first_name and last_name but only full_name is readable
            'last_name': {'write_only': True},
            }

	def get_full_name(self, obj):
		return obj.get_full_name()
