from django.urls import path

from core import views

urlpatterns = [
    path('buildings/', views.BuildingListCreate.as_view(), name='building-list-create'),
    path('buildings/<int:pk>/', views.BuildingRetrieveUpdateDestroy.as_view(), name='building-detail'),
    path('rooms/', views.RoomListCreate.as_view(), name='room-list-create'),
    path('rooms/<int:pk>/', views.RoomRetrieveUpdateDestroy.as_view(), name='room-detail'),
    path('residents/', views.ResidentListCreate.as_view(), name='resident-list-create'),
    path('residents/<int:pk>/', views.ResidentRetrieveUpdateDestroy.as_view(), name='resident-detail'),
]
