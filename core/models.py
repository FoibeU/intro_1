from django.db import models

class Building(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    capacity = models.IntegerField()  # Total number of residents the building can accommodate
    manager_name = models.CharField(max_length=100, null=True, blank=True)  # Building manager’s name
    phone_number = models.CharField(max_length=15, null=True, blank=True)  # Contact number for the building
    operational_hours = models.CharField(max_length=100, null=True, blank=True)  # Opening and closing times
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Room(models.Model):
    building = models.ForeignKey(Building, related_name='rooms', on_delete=models.CASCADE)
    room_number = models.CharField(max_length=10)
    floor = models.IntegerField()
    capacity = models.IntegerField(default=1)  # How many residents can the room accommodate
    room_type = models.CharField(max_length=50, choices=[('single', 'Single'), ('double', 'Double'), ('suite', 'Suite')])  # Room types
    is_vacant = models.BooleanField(default=True)  # Whether the room is currently vacant
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Room {self.room_number} in {self.building.name}"

class Resident(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    room = models.ForeignKey(Room, related_name='residents', on_delete=models.CASCADE)
    move_in_date = models.DateField()
    move_out_date = models.DateField(null=True, blank=True)  # Expected move-out date
    lease_duration = models.CharField(max_length=50, null=True, blank=True)  # Length of the lease (e.g., '6 months', '1 year')
    emergency_contact_name = models.CharField(max_length=100, null=True, blank=True)
    emergency_contact_phone = models.CharField(max_length=15, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
