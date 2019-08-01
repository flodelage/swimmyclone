from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from rent.models import Pool, Booking, Profile
from rent.forms import CreatePoolForm, CreateBookingForm, UserForm, ProfileForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required


def home(request):
    pools = Pool.objects.all()
    sliced_pools = pools[0:3]

    if request.method == 'POST':
        pool_form = CreatePoolForm(request.POST)

        if pool_form.is_valid():
            pool = pool_form.save(commit=False)
            pool.user = current_user
            pool.save()
    else:
        pool_form = CreatePoolForm()

    context = {
        'pools': pools,
        'sliced_pools': sliced_pools,
        'pool_form': pool_form,
    }

    return render(request, 'rent/home.html', context)


def pool_list(request):
    pools = Pool.objects.all()

    context = {
        'pools': pools,
    }

    return render(request, 'rent/pool_list.html', context)


def pool_detail(request, pool_pk):
    pool = Pool.objects.get(pk=pool_pk)
    booking_form = CreateBookingForm()

    context = {
        'pool': pool,
        'booking_form': booking_form,
    }

    return render(request, 'rent/pool_detail.html', context)


@login_required
def create_pool(request):
    if request.method == 'POST':
        pool_form = CreatePoolForm(request.POST)

        if pool_form.is_valid():
            pool = pool_form.save(commit=False)
            pool.user = request.user
            pool.save()
    else:
        pool_form = CreatePoolForm()

    context = {
        'pool_form': pool_form,
    }

    return render(request, 'rent/create_pool.html', context)



# Logs and Authentication :

def index(request):
    return render(request, 'rent/index.html')


@login_required
def special(request):
    return HttpResponse("You are logged in !")


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = ProfileForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'image' in request.FILES:
                print('found it')
                profile.image = request.FILES['image']
            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = ProfileForm()
    return render(request, 'rent/registration.html',
                  {'user_form': user_form, 'profile_form': profile_form, 'registered': registered}
                  )


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username, password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'rent/login.html', {})


