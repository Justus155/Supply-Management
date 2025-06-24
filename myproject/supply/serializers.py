from rest_framework import  serializers
from .models import *
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password


class clinicSignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clinic
        fields = ('clinic_license','name' 'password')
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return ClinicSignUp.objects.create(**validated_data)

class ClinicSerializer(serializers.ModelSerializer):
    class Meta:
        model = clinicSignIn
        fields = ('clinic_license', 'password')

