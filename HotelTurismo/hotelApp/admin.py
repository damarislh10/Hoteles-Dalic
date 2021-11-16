from django.contrib     import admin
from .models.user       import User
from .models.hotel      import Hotel

admin.site.register(User)
admin.site.register(Hotel)
# Register your models here.
