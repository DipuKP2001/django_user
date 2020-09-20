from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse
from django.contrib import messages
from .forms import UserRegistrationForm

def home(request):
    return HttpResponse('HOME PAGE')

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = UserRegistrationForm()
    context = {'form':form}
    return render(request, 'user_app/register.html', context)
