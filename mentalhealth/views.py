from django.shortcuts import render, redirect 
from .forms import RegisterForm
from django.contrib.auth import login, logout, authenticate
from .models import Resources


# Create your views here.
def home(request): 
    resources = Resources.objects.all()

    context = {
        "resources":resources
    }
    return render(request, 'main/home.html', context)

def signup(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/home')
    else:
        form = RegisterForm()
    
    return render(request, 'registration/signup.html', {"form":form})