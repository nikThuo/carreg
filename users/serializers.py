from rest_framework import serializers

from users.models import User_Roles, User_Type, Authority, Agent, Owner

class UserRolesSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_Roles
        fields = ['role_id', 'role_name']

class UserTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_Type
        fields = ['user_type_id', 'user_name', 'role']

class AuthoritySerializer(serializers.ModelSerializer):
    class Meta:
        model = Authority
        fields = ['id', 'name', 'user_type']

class AgentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agent
        fields = ['id', 'name', 'kra_pin', 'user_type']

class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner
        fields = ['national_id', 'fullname', 'gender', 'phone', 'email', 'dob', 'kra_pin', 'user_type']




