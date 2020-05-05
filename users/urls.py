from django.urls import path

from users import views

urlpatterns = [
    path('list', views.role_list, name='create'),
    path('details/<int:id>', views.role_rud, name='details'),
    path('type', views.type_list, name='create'),
    path('type_details/<int:id>', views.type_rud, name='type_details'),
    path('authority', views.authority_list, name='create'),
    path('authority_details/<int:id>', views.authority_rud, name='authority_details'),
    path('agent', views.agent_list, name='create'),
    path('agent_details/<int:id>', views.agent_rud, name='agent_details'),
    path('owner', views.owner_list, name='create'),
    path('owner_details/<int:id>', views.owner_rud, name='owner_details'),

    path('signin', views.login, name='signin'),
    path('osignup', views.owner_register, name='osignup'),
    path('asignup', views.agent_register, name='asignup'),
    path('home', views.index, name='home'),
]