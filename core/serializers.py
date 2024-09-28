from rest_framework import serializers
from .models import Resident, Room, Building

class BuildingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Building
        fields = ['id', 'name', 'address', 'capacity', 'manager_name', 'phone_number', 'operational_hours']


class RoomSerializer(serializers.ModelSerializer):
    building = BuildingSerializer(read_only=True)  # Nested serializer for building details

    class Meta:
        model = Room
        fields = ['id', 'building', 'room_number', 'floor', 'capacity', 'room_type', 'is_vacant']


class ResidentSerializer(serializers.ModelSerializer):
    room = RoomSerializer(read_only=True)  # Nested serializer for room details

    class Meta:
        model = Resident
        fields = ['id', 'name', 'email', 'phone_number', 'room', 'move_in_date', 'move_out_date', 'lease_duration', 'emergency_contact_name', 'emergency_contact_phone', 'created_at', 'updated_at']

