from django.urls import path
from .import views

urlpatterns = [
    path("", views.home, name='home'),
    path("log_in", views.log_in, name='log_in'),
    path("course_list", views.course_list, name='course_list')
]
