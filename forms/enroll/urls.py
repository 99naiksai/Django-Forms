from django.urls import path
from . import views
urlpatterns=[
    path( 'registration/', views.showformdata),
    path('success/' , views.thank_you)
    ]