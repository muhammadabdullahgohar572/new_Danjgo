
from django.http import HttpResponse
from django.shortcuts import render



def Home(request):
  return  HttpResponse("This is  a Home Page")


   
def About(request):
    return render (request,'website/index.html')



   
def Contact_us(request):
   return HttpResponse("This is  a Contact_us Page")


   
def Login(request):
  return  HttpResponse("This is  a Login Page")



   