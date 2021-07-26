from django.urls import path 
from . import views 

urlpatterns = [
    path('', views.WebToPdfConverterView.as_view(), name='converter'),
]
