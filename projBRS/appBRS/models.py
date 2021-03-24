from django.db import models
from django.contrib.auth.models import User

class userInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mobile_number = models.CharField(max_length=12)
    proof_of_user = models.CharField(max_length=20)

    def __str__(self):
        return self.user.username

class Station(models.Model):
    station_id = models.AutoField(primary_key=True)
    station_adress = models.CharField(max_length=50)
    station_phoneNo=models.CharField(max_length=10)
    bikeQuantity=models.PositiveIntegerField()
    
    def __str__(self):
        return self.station_id

class Bike(models.Model):
    BIKE_COLOR_CHOICES = [
        ("Red", "Red"),
        ("White", "White"),
        ("Black", "Black"),
        ("Blue", "Blue"),
    ]

    BIKE_TYPE_CHOICES = [
        ("Regular", "Regular"),
        ("Non Gear", "Non Gear"),
        ("Sports", "Sports"),
    ]

    bike_number = models.CharField(primary_key=True, max_length=10)
    bike_color = models.CharField(max_length=20, choices=BIKE_COLOR_CHOICES)
    bike_quantity = models.PositiveIntegerField()
    bike_type = models.CharField(max_length=20, choices=BIKE_TYPE_CHOICES)
    bike_model = models.CharField(max_length=30)
    bike_brand = models.CharField(max_length=30)
    bike_station = models.ForeignKey(Station, on_delete=models.CASCADE)

    def __str__(self):
        return self.bike_number

class Rent(models.Model):
    hourly_rent = models.PositiveIntegerField()
    daily_rent = models.PositiveIntegerField()
    weekly_rent = models.PositiveIntegerField()
    hourly_penalty = models.PositiveIntegerField()
    daily_penalty = models.PositiveIntegerField()
    weekly_penalty = models.PositiveIntegerField()
    bike_rent = models.OneToOneField(Bike, on_delete=models.CASCADE)

class Employee(models.Model): 
    station_emp = models.ForeignKey(Station, on_delete=models.CASCADE)
    employee_id = models.AutoField(primary_key=True)
    employee_name = models.CharField(max_length =20 )
    employee_phonNo = models.CharField(max_length = 10)

    def __str__(self):
        return self.employee_name

class Payment(models.Model):
    Transection_id = models.AutoField(primary_key=True)
    bill_amount=models.PositiveIntegerField()
    Payment_Des = models.CharField(max_length=100)
    Payment_user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.Transection_id
