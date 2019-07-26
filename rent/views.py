from django.shortcuts import render, get_object_or_404
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
    pool = get_object_or_404(Pool, pk=pool_pk)

    context = {
        'pool': pool,
    }

    return render(request, 'rent/pool_detail.html', context)
