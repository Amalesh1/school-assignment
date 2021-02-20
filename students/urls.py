from django.contrib import admin
from django.urls import path
from students import views

urlpatterns = [
    path("",views.home, name='home'),
    path("home",views.home,name='home'),
    path("about",views.about, name='about'),
    path("contact",views.contact, name="contact"),
    path("subjects",views.subjects, name="subjects"),
    path("teachers",views.teachers, name="teachers"),
    path("assignments",views.assignments, name="assignments"),
    path("mathassignments",views.mathassignments, name="mathassignments"),
    path("physicsassignments",views.physicsassignments, name="physicsassignments"),

]