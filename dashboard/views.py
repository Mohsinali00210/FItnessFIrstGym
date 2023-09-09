from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout 
from django.contrib import messages 
from . import models

# Create your views here.
def dashboard(request):
    if request.method == 'POST':
        useremail = request.POST['useremail']
        password = request.POST['password']
		# Authenticate
        user = authenticate(request, username=useremail, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You Have Been Logged In!")
            return redirect('dashboard')
        else:
            messages.success(request, "There Was An Error Logging In, Please Try Again...")
            return redirect('dashboard')

    else:
        return render(request, 'home.html')

def logout_view(request):
    logout(request)
    messages.success(request, "You Have Been Logged Out...")
    return redirect('dashboard')


def register_view(request):
    if request.method=='POST':
        FullName = request.POST.get('FullName')
        Email = request.POST.get('Email')
        Gender = request.POST.get('Gender')
        Phone = request.POST.get('Phone')
        Address = request.POST.get('Address')
        DateOfBirth = request.POST.get('DateOfBirth')
        FitnessGoals = request.POST.get('FitnessGoals')
        password = request.POST.get('password')
        profileP = request.FILES['ProfilePic']
        
        person = models.Person(Name=FullName,PhoneNo=Phone,Email=Email,Address=Address,DateOfBirth=DateOfBirth,Gender=Gender)
        person.save()

        registeredUser = models.RegisteredUser(PersonId=person,FitnessGoals=FitnessGoals,Image=profileP)
        registeredUser.save()
    return render(request,'register.html')