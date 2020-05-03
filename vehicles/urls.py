from django.urls import path

from vehicles import views

urlpatterns = [
    path('add_list', views.create_read_vehicle, name='create'),
    path('add_list_transactions', views.create_read_vtransactions, name='create_transactions'),
]