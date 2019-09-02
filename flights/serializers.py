from flights.models import Flight,Booking
from rest_framework import serializers

class MyListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        exclude=['miles']


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields=["id","flight","date"]

