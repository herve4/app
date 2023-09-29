from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *

# class SerializerUser(serializers.ModelSerializer):

#     class Meta:
#         model = Profiles
#         fields = '__all__'

# class SerializerUserInclude(serializers.ModelSerializer):

#     Informations = SerializerUser(source= 'profiles')

#     class Meta:
#         model = User
#         fields = '__all__'
        # fields = ('id','username','first_name','last_name','email')