from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from rent.models import Pool, Booking, Profile
from rent.forms import CreatePoolForm, CreateBookingForm, ConnexionForm, RegistrationForm
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


def inscription(request):
    if request.method == 'POST':
        account_form = RegistrationForm(request.POST)
        if account_form.is_valid():
            account_form.save()
            return redirect('home-page')
    else:
        account_form = RegistrationForm()

    context = {
        'account_form': account_form,

    }
    return render(request, 'rent/create_account.html', context)


def connexion(request):
    error = False
    if request.method == "POST":
        connexion_form = ConnexionForm(request.POST)
        if connexion_form.is_valid():
            username = connexion_form.cleaned_data["username"]
            password = connexion_form.cleaned_data["password"]
            user = authenticate(username=username,
                                password=password)  # Nous vérifions si les données sont correctes
            if user:  # Si l'objet renvoyé n'est pas None
                login(request, user)  # nous connectons l'utilisateur
            else:  # sinon une erreur sera affichée
                error = True
    else:
        connexion_form = ConnexionForm()

    context = {
        'connexion_form': connexion_form,
    }

    return render(request, 'rent/connexion.html', context)


def deconnexion(request):
    logout(request)
    return redirect(reverse(connexion))