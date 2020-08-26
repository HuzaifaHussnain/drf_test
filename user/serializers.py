from .models import User, UserProfile
from rest_framework import serializers, generics



class UserProfileSerializer(serializers.ModelSerializer):
	""" Serializer for UserProfile Model """
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


	def update(self, instance, validated_data):
		""" overriding the original update function to update the nested objects 
			Args:
				validated_data: This contains the updated data for user and userprofile models
			Return:
				instance: Returns the updated instance of user model

		"""

		if 'profile' in validated_data:
			for (key, value) in validated_data['profile'].items():
				setattr(instance.profile, key, value)
			validated_data.pop('profile')
			instance.profile.save()

		for (key, value) in validated_data.items():
			setattr(instance, key, value)
		instance.save()

		return instance

