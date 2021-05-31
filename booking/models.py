from django.db import models

# Create your models here.
class bus_info(models.Model):
    bus_name=models.CharField(max_length=100)
    plate_no=models.CharField(unique=True,max_length=13)
    AC = 'AC BUS'
    NAC = 'NON AC BUS'
    bus_type = ((AC,'AC BUS'),(NAC,'NON AC BUS'))
    type = models.CharField(choices=bus_type,default=AC,max_length=100)
    source = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    rate = models.IntegerField()
    date = models.DateField()
    boarding_time = models.TimeField()
    departure_time = models.TimeField()
    L1= models.BooleanField(default=False)
    L2 = models.BooleanField(default=False)
    L3 = models.BooleanField(default=False)
    L4 = models.BooleanField(default=False)
    L5 = models.BooleanField(default=False)
    L6 = models.BooleanField(default=False)
    L7 = models.BooleanField(default=False)
    L8 = models.BooleanField(default=False)
    L9 = models.BooleanField(default=False)
    L10 = models.BooleanField(default=False)
    L11 = models.BooleanField(default=False)
    L12 = models.BooleanField(default=False)
    L13 = models.BooleanField(default=False)
    L14 = models.BooleanField(default=False)
    L15 = models.BooleanField(default=False)
    L16 = models.BooleanField(default=False)
    L17 = models.BooleanField(default=False)
    L18 = models.BooleanField(default=False)
    U1= models.BooleanField(default=False)
    U2 = models.BooleanField(default=False)
    U3 = models.BooleanField(default=False)
    U4 = models.BooleanField(default=False)
    U5 = models.BooleanField(default=False)
    U6 = models.BooleanField(default=False)
    U7 = models.BooleanField(default=False)
    U8 = models.BooleanField(default=False)
    U9 = models.BooleanField(default=False)
    U10 = models.BooleanField(default=False)
    U11 = models.BooleanField(default=False)
    U12 = models.BooleanField(default=False)
    U13 = models.BooleanField(default=False)
    U14 = models.BooleanField(default=False)
    U15 = models.BooleanField(default=False)
    U16 = models.BooleanField(default=False)
    U17 = models.BooleanField(default=False)
    U18 = models.BooleanField(default=False)
    def __str__(self):
        return self.bus_name


class booked_seat(models.Model):
    seat_no = models.CharField(max_length=10)
    plate_no = models.CharField(max_length=100)
    user_name = models.CharField(max_length=100)
    booked_time = models.DateTimeField()           
    def __str__(self):
        return self.user_name+" "+self.seat_no+" "+self.plate_no

class passenger_detail(models.Model):
    seat_no = models.CharField(max_length=10)
    passenger_name = models.CharField(max_length=100)
    email = models.EmailField()
    mobile_no = models.IntegerField()
    age = models.IntegerField()
    gender = models.CharField(max_length=5)
    booked_by = models.CharField(max_length=20)
    source = models.CharField(max_length=20)
    destination = models.CharField(max_length=20)
    bus_plate_no = models.CharField(max_length=13)
    bus_name = models.CharField(max_length=50)
    def __str__(self):
        return self.passenger_name