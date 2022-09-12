import http
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django import forms
from predict.forms import size_form
import pandas as pd
import numpy as np 
import joblib



#def Capture(request):
#    if request.method == 'POST':
#        data=size_form(request.POST)
#        if data.is_valid():   
#            saple_length=data.cleaned_data["saple_length"]
#            saple_width=data.cleaned_data["saple_width"]
#            patle_length=data.cleaned_data["patle_length"]
#            patle_width=data.cleaned_data["patle_width"]
#            model=joblib.load("model_joblib.pkl")
#            result=model.predict([[saple_length,saple_width,patle_length,patle_width]])
#            if result[0]==0:
#                result='Setosa'
#            if result[0]==1:
#                result='Verscicolor'
#            if result[0]==2:
#                result='Virginica'
#            return render(request,'predict/result.html',{'result':result})
#            
#            
#    else:
#        data=size_form()        
#    return render(request,'predict/predict.html',{'form':data})


def Capture(request):
    if request.method == 'POST':
        Data={}
        Data['saple_length']=request.POST["Saple_Length"]
        Data['saple_width']=request.POST["Saple_Width"]
        Data['patle_length']=request.POST["Patle_Length"]
        Data['patle_width']=request.POST["Patle_Width"]
        model=joblib.load("model_joblib.pkl")
        result=model.predict([[Data['saple_length'],Data['saple_width'],Data['patle_length'],Data['patle_width']]])
        if result[0]==0:
            Data['result']='Setosa'
        if result[0]==1:
            Data['result']='Verscicolor'
        if result[0]==2:
            Data['result']='Virginica'
        return render(request,'predict/result.html',Data)
            
    else:
        data=size_form()        
    return render(request,'predict/predict.html',{'form':data})
