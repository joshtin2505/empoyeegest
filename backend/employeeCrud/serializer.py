from rest_framework import serializers
from .models import Employee, Phone, Email


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        # fields = (
        #     "id",
        #     "name",
        #     "email",
        #     "monthlySalary",
        #     "dni_type",
        #     "dni",
        #     "position",
        #     "startDate",
        #     "departament",
        #     "addedBy",
        # )
        fields = "__all__"


class PhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phone
        fields = "__all__"

class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Email
        fields = "__all__"