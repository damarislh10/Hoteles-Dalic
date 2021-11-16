from hotelApp.models.hotel    import Hotel
from rest_framework           import serializers

class HotelSerializer(serializers.ModelSerializer):
    # configuración interna de la otra clase
    class Meta: 
        model = Hotel # que modelos y que campos va a extraer
        fields = ['id','nombreHotel','descripcion','ubicacion','calificacion', 'precio']