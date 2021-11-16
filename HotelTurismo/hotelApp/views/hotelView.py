
from django.db.models.query                  import QuerySet
from django.http                             import response
from rest_framework                          import views, status
from rest_framework.response                 import Response
from rest_framework                          import generics
from rest_framework                          import generics
from hotelApp.models.hotel                   import Hotel
from hotelApp.serializers.hotelSerializer    import HotelSerializer


# listado y creación de todos los hoteles
# List, create 
class HotelListCreateView(generics.ListCreateAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer

# Read, update, delete
class HotelRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset= Hotel.objects.all()
    serializer_class = HotelSerializer
