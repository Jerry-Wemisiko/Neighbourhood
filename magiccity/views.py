from django.shortcuts import render
from magiccity.models import Neighbourhood,Post,Business
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='/accounts/login/')
def homepage(request):
    houses = Neighbourhood.objects.all()

    return render(request, 'index.html',{'houses':houses})

