from django.shortcuts import render,reverse
from django.contrib import messages
from .models import Profiles_mongo_data
from django.shortcuts import render
from rest_framework import viewsets
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required
from .models import Profile_sqll,Profiles_mongo_data
from .forms import LoginForm
from tracker.templates import tracker


""" from .serializers import ProfilesSerializer
from rest_framework_mongoengine import viewsets as mongo_viewsets
class ProfilesViewSet(mongo_view_sets.ModelViewSet):
    queryset=Profiles_mongo_data.objects.all()
    serializer_class=ProfilesSerializer """
def register_view(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        Profiles_mongo_data(
            username=form.cleaned_data['username'],
            email=form.cleaned_data['email'],
            password=form.cleaned_data['password'], 
            age=form.cleaned_data['age'],
            weight=form.cleaned_data['weight'],
            height=form.cleaned_data['height']
        ).save()
        #return redirect('register_users_list')
        return redirect('login')
    return render(request, 'registration_app/register.html', {'form': form})

def register_users_list(request):
    registers=Profiles_mongo_data.objects.all()
    return render(request,'registration_app/register_list.html',{'employees':registers})

def login_view(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']

        try:
            user = Profiles_mongo_data.objects.get(username=username, password=password)
            request.session['mongo_user'] = user.username  # Session login
            request.session['username'] = user.username
            request.session['password'] = user.password
            #return redirect(reverse('login_users_list', kwargs={'username': user.username})) # Replace with your desired page
            return redirect('dashboard')
        except Profiles_mongo_data.DoesNotExist:
            messages.error(request, "Invalid username or password.")

    return render(request, 'registration_app/login.html', {'form': form})
def login_users_list(request, username):
    try:
        user = Profiles_mongo_data.objects.get(username=username)
        
        return render(request, 'registration_app/register_list.html', {'employees': [user]})
    except Profiles_mongo_data.DoesNotExist:
        return render(request, 'registration_app/register_list.html', {'employees': []})

def dashboard_view(request):
    username = request.session.get('username')
    email = request.session.get('email')

    if not username:
        return redirect('login')

    user = Profiles_mongo_data.objects.get(username=username)
    return render(request, 'tracker/dashboard.html', {'user': user})




def logout_view(request):
    request.session.flush()  # Clear all session data
    return redirect('login')


# Create your views here.



