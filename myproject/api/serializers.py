from rest_framework import serializers
from supply.models import Clinic

class ClinicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clinic
        fields=('clinic_license', 'name', 'email', 'password')
        extra_kwargs = {
            'password': {'write_only': True}
        }
    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return Clinic.objects.create(**validated_data)
    
class ClinicSignInSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clinic
        fields = ('clinic_license', 'password')
        extra_kwargs = {
            'password': {'write_only': True}
        }
    
    def validate(self, data):
        clinic_license = data.get('clinic_license')
        password = data.get('password')
        
        if not clinic_license or not password:
            raise serializers.ValidationError("Clinic license and password are required.")
        
        return data    