from django.contrib import admin
from .models import bus_info,booked_seat,passenger_detail
# Register your models here.
admin.site.register(bus_info)
admin.site.register(booked_seat)
admin.site.register(passenger_detail)