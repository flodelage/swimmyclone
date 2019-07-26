from django.shortcuts import render
from django.http import HttpResponseRedirect

from rent.models import Pool
from django.contrib.auth.models import User

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
