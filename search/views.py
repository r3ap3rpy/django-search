from django.shortcuts import render
from .models import Goods
from django.db.models import Q
# Create your views here.
def search(request):
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
        goods = Goods.objects.distinct().filter(Q(name__icontains=search_query) |Q(description__icontains=search_query))

        return render(request, 'search/index.html', {'goods':goods})

    else:  
        goods = Goods.objects.all()
        return render(request, 'search/index.html',{'goods':goods})