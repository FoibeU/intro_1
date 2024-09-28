from rest_framework import generics
from drf_yasg.utils import swagger_auto_schema
from .models import Resident, Room, Building
from .serializers import ResidentSerializer, RoomSerializer, BuildingSerializer

class BuildingListCreate(generics.ListCreateAPIView):
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer

    @swagger_auto_schema(
        operation_description="List all buildings or create a new building.",
        responses={200: BuildingSerializer(many=True), 201: BuildingSerializer},
        request_body=BuildingSerializer,
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        request_body=BuildingSerializer,
        responses={201: BuildingSerializer}
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

class BuildingRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer

    @swagger_auto_schema(
        operation_description="Retrieve, update or delete a building.",
        responses={200: BuildingSerializer, 204: None, 404: "Not Found"}
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        request_body=BuildingSerializer,
        responses={200: BuildingSerializer, 404: "Not Found"}
    )
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @swagger_auto_schema(
        responses={204: None, 404: "Not Found"}
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

class RoomListCreate(generics.ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

    @swagger_auto_schema(
        operation_description="List all rooms or create a new room.",
        responses={200: RoomSerializer(many=True), 201: RoomSerializer},
        request_body=RoomSerializer,
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        request_body=RoomSerializer,
        responses={201: RoomSerializer}
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

class RoomRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

    @swagger_auto_schema(
        operation_description="Retrieve, update or delete a room.",
        responses={200: RoomSerializer, 204: None, 404: "Not Found"}
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        request_body=RoomSerializer,
        responses={200: RoomSerializer, 404: "Not Found"}
    )
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @swagger_auto_schema(
        responses={204: None, 404: "Not Found"}
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

class ResidentListCreate(generics.ListCreateAPIView):
    queryset = Resident.objects.all()
    serializer_class = ResidentSerializer

    @swagger_auto_schema(
        operation_description="List all residents or create a new resident.",
        responses={200: ResidentSerializer(many=True), 201: ResidentSerializer},
        request_body=ResidentSerializer,
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        request_body=ResidentSerializer,
        responses={201: ResidentSerializer}
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

class ResidentRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Resident.objects.all()
    serializer_class = ResidentSerializer

    @swagger_auto_schema(
        operation_description="Retrieve, update or delete a resident.",
        responses={200: ResidentSerializer, 204: None, 404: "Not Found"}
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        request_body=ResidentSerializer,
        responses={200: ResidentSerializer, 404: "Not Found"}
    )
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @swagger_auto_schema(
        responses={204: None, 404: "Not Found"}
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)
