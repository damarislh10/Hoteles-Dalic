from django.db.models import fields
from rest_framework import serializers
from hotelApp.models.user import User,UserManager


# clase serializador y hereda clase
class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['is_superuser','id', 'username', 'password', 'name', 'email']



def create(self, validated_data):
    userInstance = User.objects.create(**validated_data)
    return userInstance


def to_representation(self, obj):
    user = User.objects.get(id=obj.id)
    return {
        'is_superuser': user.is_superuser,
        'id': user.id,
        'username': user.username,
        'name': user.name,
        'email': user.email,
    }


