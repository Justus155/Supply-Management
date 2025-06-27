from rest_framework import serializers
from .models import clinic

class ClinicSerializer(serializers.ModelSerializer):
    class Meta:
        model=clinic
        fields = [ 'name', 'license_number', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

        def create(self, validated_data):
            user=clinic(
                name=validated_data['name'],
                license_number=validated_data['license_number'],
            )
            user.set_password(validated_data['password'])
            user.save()
            return user