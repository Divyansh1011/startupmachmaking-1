from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('applicant', views.applicantdashboard, name="applicantdashboard"),
    path('joblist', views.joblist, name="joblist")
] 
