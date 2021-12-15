from rest_framework import serializers

from .models import Driver, Vehicle


class DriverSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format='%d/%m/%Y %H:%M:%S', required=False)
    updated_at = serializers.DateTimeField(format='%d/%m/%Y %H:%M:%S', required=False)
    class Meta:
        model = Driver
        fields = '__all__'

class VehicleSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format='%d/%m/%Y %H:%M:%S', required=False)
    updated_at = serializers.DateTimeField(format='%d/%m/%Y %H:%M:%S', required=False)
    class Meta:
        model = Vehicle
        fields = '__all__'

class VehicleDriverSerializer(serializers.Serializer):
    driver = serializers.IntegerField(source='Driver.id', allow_null=True)