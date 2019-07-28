from django.shortcuts import render
from django.http import HttpResponseRedirect

from rent.models import Pool
from rent.forms import CreatePoolForm
from django.contrib.auth.models import User


def home(request):
    pools = Pool.objects.all()
    sliced_pools = pools[0:3]

    context = {
        'pools': pools,
        'sliced_pools': sliced_pools,
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

    context = {
        'pool': pool,
    }

    return render(request, 'rent/pool_detail.html', context)


def create_pool(request):
    if request.method == 'POST':
        pool_form = CreatePoolForm(request.POST)

        if pool_form.is_valid():
            pool = pool_form.save(commit=False)
            pool.user = current_user
            pool.save()
    else:
        pool_form = CreatePoolForm()

    context = {
        'pool_form': pool_form,
    }

    return render(request, 'rent/create_pool.html', context)



