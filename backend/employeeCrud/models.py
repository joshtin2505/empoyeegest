from django.db import models
# import uuid
from django.utils.translation import gettext_lazy as _
# Create your models here.

# class Employee(models.Model):

#     class DNIType(models.TextChoices):
#         NIT = "NIT", _("NIT")
#         CC = "CC", _("Cédula de Ciudadanía")

#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     name = models.CharField(max_length=100)
#     email = models.EmailField(unique=True)
#     monthlySalary = models.DecimalField(max_digits=10, decimal_places=2)
#     dni_type = models.CharField(
#         max_length=3, choices=DNIType.choices, default=DNIType.CC
#     )
#     dni = models.CharField(max_length=20, unique=True)
#     position = models.CharField(max_length=100)
#     startDate = models.DateField()
#     departament = models.CharField(max_length=100)
#     addedBy = models.ForeignKey(
#         User, on_delete=models.CASCADE, related_name="employees_added"
#     )

#     class Meta:
#         verbose_name = _("employee")
#         verbose_name_plural = _("employees")

#     def __str__(self):
#         return f"{self.name} - {self.position}"

# class Phone(models.Model):
  
#   class PhoneType(models.TextChoices):
#     CEL = "CEL", _("Celular")
#     TEL = "TEL", _("Fijo")  
    
#   id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#   type = models.CharField(
#     max_length=3, choices=PhoneType.choices, default=PhoneType.CEL
#   )
#   number = models.CharField(max_length=20)
#   employee = models.ForeignKey(
#     Employee, on_delete=models.CASCADE, related_name="phones"
#   )
#   areaCode = models.CharField(max_length=5, blank=True, null=True)

#   class Meta:
#     verbose_name = _("phone")
#     verbose_name_plural = _("phones")
  
#   def __str__(self):
#     return self.number

# class Email(models.Model):
  # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  # email = models.EmailField()
  # employee = models.ForeignKey(
  #   Employee, on_delete=models.CASCADE, related_name="emails"
  # )
  
  # class Meta:
  #   verbose_name = _("email")
  #   verbose_name_plural = _("emails")
    
  # def __str__(self):
  #   return self.email