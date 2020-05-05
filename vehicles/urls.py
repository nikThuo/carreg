from django.urls import path

from vehicles import views

urlpatterns = [
    path('add_list', views.create_read_vehicle, name='create'),
    path('add_list_transactions', views.create_read_vtransactions, name='create_transactions'),

    path('vehicle_registration', views.vehicle_registration, name='vehicle_registration'),
    path('vehicle_registration_details', views.vehicle_registration_details, name='vehicle_registration_details'),
    path('vehicle_transfer', views.vehicle_transfer, name='vehicle_transfer'),
    path('vehicle_transfer_details', views.vehicle_transfer_details, name='vehicle_transfer_details'),
    path('vehicle_confirm', views.vehicle_confirm, name='vehicle_confirm'),
    path('vehicle_confirm_details', views.vehicle_confirm_details, name='vehicle_confirm_details'),
]