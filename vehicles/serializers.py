from rest_framework import serializers
from rest_framework.response import Response
from rest_framework import status

from vehicles.models import Vehicles, Transactions

import hashlib as hasher
import pickle

def hash_block(block):
    sha = hasher.sha3_256()
    sha.update(pickle.dumps(block))
    m = sha.hexdigest()

    return m

class VehiclesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicles
        fields = ['transaction_id', 'car_reg_no', 'car_make', 'car_type', 'car_model', 'hash', 'timestamp']

    def retrieve(self):
        serializer = VehiclesSerializer(self, many=True)
        return serializer

    def create(self, validated_data):
        # hash = hash_block(validated_data)

        car_search = Vehicles.objects.filter(car_reg_no=validated_data['car_reg_no'].upper()).values('car_reg_no').exists()
        # car_search2 = Vehicles.objects.get(car_reg_no=validated_data['car_reg_no'].upper())
        print('--------->', car_search)
        # print('--------->', car_search2)
        print('--------->', validated_data['car_reg_no'])
        if car_search:
            return Response({'error': 'Vehicle Exists'})
            print('--------->', car_search[0]['car_reg_no'])
            # return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            hash = hash_block(validated_data)
            reg_no = validated_data['car_reg_no']
            make = validated_data['car_make']
            car_type = validated_data['car_type']
            model = validated_data['car_model']

            vehicle = Vehicles.objects.create(
                car_reg_no = reg_no,
                car_make = make,
                car_type = car_type,
                car_model = model,
                hash = hash
            )

            return vehicle
            
class TransactionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transactions
        fields = ['transaction_id', 'car_reg', 'national', 'kra', 'status', 'previous_hash', 'hash', 'timestamp']

    # def retrieve(self):
    #     serializer = TransactionsSerializer(self, many=True)
    #     return serializer
    
    # def create(self, validated_data):
    #     car_search = Transactions.objects.filter(car_reg=validated_data['car_reg'].upper()).values('car_reg').exists()
    #     if car_search:
    #         return Response({'error': 'Vehicle Exists'})
    #     else:
    #         reg_no = Vehicles.objects.get(car_reg_no=validated_data['car_reg'].upper())
    #         print('-------->', reg_no)
    #         print('-------->', reg_no[0])
    #         car_reg = reg_no[0].get('car_reg_no')
    #         car_hash = reg_no[0].get('hash')
    #         print('-------->', car_reg, '<------->', car_hash)

    #         hash = hash_block(validated_data)
    #         reg_no = car_reg
    #         id = validated_data['national']
    #         status = 'owned'
    #         phash = car_hash

    #         transactions = Transactions.objects.create(
    #             car_reg = reg_no,
    #             national = id,
    #             status = status,
    #             previous_hash = phash,
    #             hash = hash
    #         )

    #         return transactions

            