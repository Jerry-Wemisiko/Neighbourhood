from magiccity.forms import BusinessForm, SignupForm,UserProfileForm,NeighbourHoodForm,PostForm
from django.shortcuts import get_object_or_404, render
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
@login_required(login_url='/accounts/login/')
def visit_neighbourhood(request, id):
    neighbourhood = Neighbourhood.objects.get(id=id)
    business = Business.objects.filter(neighbourhood_id=id)

    if request.method == 'POST':
        form = BusinessForm(request.POST)
        if form.is_valid():
            b_form = form.save(commit=False)
            b_form.neighbourhood = neighbourhood
            b_form.user = request.user.profile
            b_form.save()
            return redirect('viewhood', id)
    else:
        form = BusinessForm()
    context = {
        'neighbourhood': neighbourhood,
        'form': form,
        'business': business,
    }
    return render(request, 'viewhood.html', context)


@login_required(login_url='/accounts/login/')  
def bepartof_neighbourhood(request,id):
    house = get_object_or_404(Neighbourhood,id = id)
    request.user.profile.neighbourhood = house
    request.user.profile.save()
    return redirect('homepage')

@login_required(login_url='/accounts/login/')
def exit_neighbourhood(request, id):
    neighbourhood = get_object_or_404(Neighbourhood, id=id)
    request.user.profile.neighbourhood = None
    request.user.profile.save()
    messages.success(
        request, 'Sorry to let you go')
    return redirect('homepage')

@login_required(login_url='/accounts/login/')
def new_post(request, house_id):
    neighbourhood = Neighbourhood.objects.get(id=house_id)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.neighbourhood = neighbourhood
            post.user = request.user.profile
            post.save()
            messages.success(
                    request, 'You have succesfully created a Post')
            return redirect('single-hood', house_id)
    else:
        form = PostForm()
    return render(request, 'post.html', {'form': form})


@login_required(login_url='/accounts/login/')
def search_business(request):
    if 'bizz_name' in request.GET and request.GET["bizz_name"]:
        search_term = request.GET.get("bizz_name")
        found_businesses = Business.search_by_name(search_term)
        message = f"{search_term}"
        print(search_term)
        context = {"found_business":found_businesses,"message":message}
        return render(request, 'search.html',context)
    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})