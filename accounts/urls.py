from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    MyTokenObtainPairView,
    RegisterPatientView,
    RegisterDoctorView,
    update_user,
    reset_password,
    forget_password,
    user_info,
)


urlpatterns = [
    path("token/", MyTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("register/patient/", RegisterPatientView.as_view(), name="register_patient"),
    path("register/doctor/", RegisterDoctorView.as_view(), name="register_doctor"),
    path("update_user/", update_user),
    path("forget_password/", forget_password),
    path("reset_password/<str:token>/", reset_password),
    path("user_info/", user_info),
]


# urlpatterns += router.urls