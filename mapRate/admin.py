from django.contrib import admin

# Register your models here.
from .models import Bathroom, Rating, Pin

# Register your models here.
admin.site.register(Bathroom)
admin.site.register(Rating)
admin.site.register(Pin)