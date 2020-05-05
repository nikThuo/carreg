from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from users.models import User_Roles, User_Type, Authority, Agent, Owner
from users.serializers import UserRolesSerializer, UserTypeSerializer, AuthoritySerializer, AgentSerializer, OwnerSerializer

# Create your views here.
############# ------------ UI ------------ #############
############# ------------ Sign In ------------ #############
def login(request):
    return render(request, template_name='carreg/sign_in.html')

############# ------------ Owner Sign Up ------------ #############
def owner_register(request):
    return render(request, template_name='carreg/owner_sign_up.html')

############# ------------ Agent Sign Up ------------ #############
def agent_register(request):
    return render(request, template_name='carreg/agent_sign_up.html')

############# ------------ Home ------------ #############
def index(request):
    return render(request, template_name='carreg/index.html')


############# ------------ USER ROLES ------------ #############
@api_view(['GET', 'POST'])
def role_list(request):
    """
    List or create a user role(s)
    """
    if request.method == 'GET':
        roles = User_Roles.objects.all()
        serializer = UserRolesSerializer(roles, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = UserRolesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def role_rud(request, id=None):
    """
    Retrieve, update or delete a user role
    """
    try:
        roles = User_Roles.objects.get(pk=id)
    except User_Roles.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        if roles:
            serializer = UserRolesSerializer(product)
            return Response(serializer.data)
        else:
            #id = None
            roles1 = User_Roles.objects.all(id=None)
            serializer = UserRolesSerializer(roles1, many=True)
            return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = UserRolesSerializer(roles, data=request.data)
        if serializer.is_valid():
            serializer.save()
            print('&&&&&&&&&&&', serializer.data)
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        roles.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


############# ------------ USER TYPES ------------ #############
@api_view(['GET', 'POST'])
def type_list(request):
    """
    List or create a user type(s)
    """
    if request.method == 'GET':
        types = User_Type.objects.all()
        serializer = UserTypeSerializer(types, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = UserTypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def type_rud(request, id=None):
    """
    Retrieve, update or delete a user type
    """
    try:
        types = User_Type.objects.get(pk=id)
    except User_Type.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        if types:
            serializer = UserTypeSerializer(product)
            return Response(serializer.data)
        else:
            #id = None
            types1 = User_Type.objects.all(id=None)
            serializer = UserTypeSerializer(types1, many=True)
            return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = UserTypeSerializer(types, data=request.data)
        if serializer.is_valid():
            serializer.save()
            print('&&&&&&&&&&&', serializer.data)
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        types.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


############# ------------ AUTHORITY ------------ #############
@api_view(['GET', 'POST'])
def authority_list(request):
    """
    List or create an authority
    """
    if request.method == 'GET':
        authority = Authority.objects.all()
        serializer = AuthoritySerializer(authority, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = AuthoritySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def authority_rud(request, id=None):
    """
    Retrieve, update or delete an authority
    """
    try:
        authority = Authority.objects.get(pk=id)
    except Authority.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        if authority:
            serializer = AuthoritySerializer(product)
            return Response(serializer.data)
        else:
            #id = None
            authority1 = Authority.objects.all(id=None)
            serializer = AuthoritySerializer(authority1, many=True)
            return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = AuthoritySerializer(authority, data=request.data)
        if serializer.is_valid():
            serializer.save()
            print('&&&&&&&&&&&', serializer.data)
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        authority.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


############# ------------ AGENTS ------------ #############
@api_view(['GET', 'POST'])
def agent_list(request):
    """
    List or create an agent(s)
    """
    if request.method == 'GET':
        agent = Agent.objects.all()
        serializer = AgentSerializer(agent, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = AgentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def agent_rud(request, id=None):
    """
    Retrieve, update or delete an agent
    """
    try:
        agent = Agent.objects.get(pk=id)
    except Agent.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        if agent:
            serializer = AgentSerializer(product)
            return Response(serializer.data)
        else:
            #id = None
            agent1 = Agent.objects.all(id=None)
            serializer = AgentSerializer(agent1, many=True)
            return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = AgentSerializer(agent, data=request.data)
        if serializer.is_valid():
            serializer.save()
            print('&&&&&&&&&&&', serializer.data)
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        agent.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


############# ------------ OWNERS ------------ #############
@api_view(['GET', 'POST'])
def owner_list(request):
    """
    List or create an owner(s)
    """
    if request.method == 'GET':
        owner = Owner.objects.all()
        serializer = OwnerSerializer(owner, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = OwnerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def owner_rud(request, id=None):
    """
    Retrieve, update or delete an owner
    """
    try:
        owner = Owner.objects.get(pk=id)
    except Owner.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        if owner:
            serializer = OwnerSerializer(owner)
            return Response(serializer.data)
        else:
            #id = None
            owner1 = Owner.objects.all(id=None)
            serializer = OwnerSerializer(owner1, many=True)
            return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = OwnerSerializer(owner, data=request.data)
        if serializer.is_valid():
            serializer.save()
            print('&&&&&&&&&&&', serializer.data)
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        owner.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
