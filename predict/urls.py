from django.urls import path
from predict import views

app_name='predict'

urlpatterns = [
    path("",views.Capture,name='predict'),
    
    ]