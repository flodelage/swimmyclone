from django.shortcuts import render
from django.http import HttpResponseRedirect

from rent.models import Pool
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
