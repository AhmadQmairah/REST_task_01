from rest_framework.generics import ListAPIView
from .models import Flight,Booking
from django.utils import timezone
from .serializers   import MyListSerializer,BookingSerializer





class ListView(ListAPIView):
    queryset = Flight.objects.all()
    serializer_class = MyListSerializer



class BookingView(ListAPIView):
    queryset = Booking.objects.filter(date__gte=timezone.now())
    serializer_class = BookingSerializer






