from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class RoomType(models.Model):
    title = models.CharField(max_length=20)
    details = models.JSONField(null=True)

    def __str__(self):
        return self.title
    
class Room(models.Model):
    room_type = models.ForeignKey(RoomType, on_delete=models.CASCADE)
    room_number = models.CharField(max_length=100)
    description = models.TextField(null=True)

    def __str__(self):
        return f"{self.room_number} - {self.room_type}"

class Booking(models.Model):
    room_number = models.ForeignKey(Room, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    booking_date = models.DateTimeField(auto_now_add=True)
    total_guest = models.IntegerField()
    checkin_date = models.DateField()
    checkout_date = models.DateField()
    booking_amount = models.DecimalField(max_digits=10, decimal_places=2)
    booking_details = models.JSONField()

    def __str__(self):
        return f"{self.room_number} - {self.user} - {self.checkin_date} - {self.checkout_date}"