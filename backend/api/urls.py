from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
import core.views as userViews  
import employeeCrud.views as employeeViews

# Configuración de rutas del router
router = DefaultRouter()
router.register(r"employees", employeeViews.EmployeeViewSet)
router.register(r"phones", employeeViews.PhoneViewSet)
router.register(r"emails", employeeViews.EmailViewSet)

# URL patterns
urlpatterns = [
    path('admin/', admin.site.urls),
    path("login/", userViews.login, name="login"),
    path("register/", userViews.register, name="register"),
    path("", include(router.urls)),
]
