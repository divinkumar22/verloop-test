from django.contrib import admin
from django.urls import path
from address.views import *

urlpatterns = [
    path('getAddressDetails',AddressDetailsView.as_view(),name='address'),
]
