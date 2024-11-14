# from rest_framework.decorators import api_view, authentication_classes, permission_classes
# from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .serializer import EmployeeSerializer, EmailSerializer, PhoneSerializer
from .models import Employee, Email, Phone

from rest_framework.viewsets import ModelViewSet


class EmployeeViewSet(ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()

class PhoneViewSet(ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = PhoneSerializer
    queryset = Phone.objects.all()

class EmailViewSet(ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = EmailSerializer
    queryset = Email.objects.all()



# @api_view(["GET"])
# @authentication_classes([TokenAuthentication])
# @permission_classes([IsAuthenticated])
# def get_employees(request):
#   return Response("Hello from get_employees")

# @api_view(["POST"])
# @authentication_classes([TokenAuthentication])
# @permission_classes([IsAuthenticated])
# def create_employee(request):
#   return Response("Hello from create_employee")

# @api_view(["PUT"])
# @authentication_classes([TokenAuthentication])
# @permission_classes([IsAuthenticated])
# def update_employee(request):
#   return Response("Hello from update_employee")

# @api_view(["DELETE"])
# @authentication_classes([TokenAuthentication])
# @permission_classes([IsAuthenticated])
# def delete_employee(request):
#   return Response("Hello from delete_employee")

# @api_view(["GET"])
# @authentication_classes([TokenAuthentication])
# @permission_classes([IsAuthenticated])
# def get_employee(request):
#   return Response("Hello from get_employee")