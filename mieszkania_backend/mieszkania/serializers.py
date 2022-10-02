from rest_framework import serializers
# models
from .models import Apartment, PriceRecord

class ApartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Apartment
        fields = '__all__'