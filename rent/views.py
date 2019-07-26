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