from django.urls import path
from . import views

urlpatterns =[
    path("",views.index, name="index"),
    path("Type-of-Login /", views.choose, name = 'choose'),
    path("User-Login/", views.login, name = 'login'),
    path("User-Signup/", views.signup, name = 'signup'),
    path("Home/", views.index, name = 'home'),
    path("Patient-Registeration/", views.PatientReg, name='patient-registeration'),
    path("Doctor-Registeration/", views.DoctorReg, name='doctor-registeration'),
    path("Patient-Registeration-Page-2/", views.PatientReg2, name='patientnext'),
]