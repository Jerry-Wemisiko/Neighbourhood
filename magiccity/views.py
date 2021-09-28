from magiccity.forms import SignupForm
from django.shortcuts import render
from magiccity.models import Neighbourhood,Post,Business
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.shortcuts import redirect

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

