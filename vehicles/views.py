from django.shortcuts import render
from django.template.defaultfilters import register
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from vehicles.models import Vehicles, Transactions
from users.models import Owner
from vehicles.serializers import VehiclesSerializer, TransactionsSerializer

import hashlib as hasher
import pickle

@register.filter(name='range')
def filter_year(start, end):
    return range(start, end)

def hash_block(block):
    sha = hasher.sha3_256()
    sha.update(pickle.dumps(block))
    m = sha.hexdigest()

    return m

# Create your views here.
############# ------------ UI ------------ #############
############# ------------ Vehicle Registration ------------ #############
def vehicle_registration(request):
    return render(request, template_name='carreg/vehicle_registration.html')

############# ------------ Vehicle Registration Details ------------ #############
def vehicle_registration_details(request):
    return render(request, template_name='carreg/vehicle_registration_details.html')

############# ------------ Vehicle Transfer ------------ #############
def vehicle_transfer(request):
    return render(request, template_name='carreg/vehicle_transfer_owner.html')

############# ------------ Vehicle Transfer Details ------------ #############
def vehicle_transfer_details(request):
    return render(request, template_name='carreg/vehicle_transfer_owner_view.html')

############# ------------ Vehicle Confirm ------------ #############
def vehicle_confirm(request):
    return render(request, template_name='carreg/vehicle_transfer_confirmation_status.html')

############# ------------ Vehicle Confirm Details ------------ #############
def vehicle_confirm_details(request):
    return render(request, template_name='carreg/vehicle_transfer_confirmation_status_view.html')


############# ------------ VEHICLES ------------ #############
@api_view(['GET', 'POST'])
def create_read_vehicle(request):
    """
    List or create a vehicle
    """
    if request.method == 'GET':
        vehicles = Vehicles.objects.all()
        serializer = VehiclesSerializer.retrieve(vehicles)
        return Response(serializer.data)

    elif request.method == 'POST':
        params = request.data
        if not request.POST._mutable:
            request.POST._mutable = True
        # print('check1----->',request.POST._mutable)

        serializer = VehiclesSerializer.create(request, request.data)
        request.POST._mutable = False

        if serializer:
            # serializer.save()
            return Response(request.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


############# ------------ VEHICLES TRANSACTIONS ------------ #############
@api_view(['GET', 'POST'])
def create_read_vtransactions(request):
    """
    List or create a vehicle
    """
    if request.method == 'GET':
        transactions = Transactions.objects.all()
        serializer = TransactionsSerializer.retrieve(transactions)
        return Response(serializer.data)

    elif request.method == 'POST':
        params = request.data
        if not request.POST._mutable:
            request.POST._mutable = True
        # print('check1----->',request.POST._mutable)
        print('Params -------->', params)
        print('Reg No -------->', params.get('car_reg'))
        car_search = Transactions.objects.filter(car_reg=request.data['car_reg'].upper()).values()
        if car_search:
            return Response({'error': 'Vehicle Exists'})
        else:
            # car = dict()
            hash = hash_block(request.data)
            reg_no = Vehicles.objects.get(car_reg_no=request.data['car_reg'])
            print('Returned Reg------>', reg_no)
            print('Returned------>', reg_no.car_reg_no)
            car_reg = reg_no.car_reg_no
            transactions = Transactions(
                car_reg = Vehicles.objects.get(car_reg_no=request.data['car_reg']),
                national = Owner.objects.get(national_id=request.data['id']),
                status = 'owned',
                previous_hash = reg_no.hash,
                hash = hash
            )

            car = {'car_reg': transactions.car_reg, 'national': transactions.national, 'status': transactions.status, 
                   'previous_hash': transactions.previous_hash, 'hash': transactions.hash}
            print('Transactions------->', transactions)
            # car.update(transactions)
            serializer = TransactionsSerializer(data=car)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # serializer = TransactionsSerializer.create(request, request.data)
        # request.POST._mutable = False

        # if serializer:
        #     # serializer.save()
        #     return Response(serializer, status=status.HTTP_201_CREATED)
        # return Response(status=status.HTTP_400_BAD_REQUEST)

