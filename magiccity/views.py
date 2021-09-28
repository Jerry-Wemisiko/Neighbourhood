from magiccity.forms import SignupForm,UserProfileForm,NeighbourHoodForm
from django.shortcuts import render
from magiccity.models import Neighbourhood,Post,Business
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.shortcuts import redirect
from django.contrib import messages

# Create your views here.
@login_required(login_url='/accounts/login/')
def homepage(request):
    houses = Neighbourhood.objects.all()

    return render(request, 'index.html',{'houses':houses})

def register(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('login')

    else:
        form= SignupForm()
    return render(request, 'auth/signup.html', {'form': form})

@login_required(login_url='/accounts/login/')    
def profile(request):
    if request.method == 'POST':
        p_form = UserProfileForm(request.POST, request.FILES, instance=request.user)
        if  p_form.is_valid():
            p_form.save()
            return redirect('home')
    else:
        profile_form = UserProfileForm(instance=request.user)
    return render(request, 'profile.html',{ "p_form": p_form})

def locations(request):
    houses = Neighbourhood.objects.all()
    houses = houses[::-1]

    return render(request, 'index.html',{'houses':houses})

@login_required(login_url='/accounts/login/')
def new_neighbourhood(request):
    if request.method == 'POST':
        form = NeighbourHoodForm(request.POST, request.FILES)
        if form.is_valid():
            neighbourhood = form.save(commit=False)
            neighbourhood.user = request.user
            neighbourhood.save()
            messages.success(request,'New house owner in the neighbourhood!')
            return redirect('homepage')
    else:
        form= NeighbourHoodForm()
    return render(request, 'new_neighbourhood.html', {'form': form})
    
def bepartof_neighbourhood(request,id):