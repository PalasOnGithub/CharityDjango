from django.shortcuts import render , redirect
from .models import Blog , EventCategory , EropStudent
from part1.models import HomeBack
import random
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

# Create your views here.

def DetailBlog(request , nek):
    try:
        context = dict()
        
        the_inf = Blog.objects.all()
        items = list(the_inf)
        hero = Blog.objects.get(fiknole = nek)
        pasthero = random.choice(items)
        nexhero = random.choice(items)
        scategories = EventCategory.objects.all()
        last_inf = the_inf[:4]

        context['her'] = hero
        context['pasther'] = pasthero
        context['nexher'] = nexhero
        context['scat'] = scategories
        context['newest_b'] = last_inf
        context['admin_pic'] = HomeBack.objects.get(pk=1)
        
    except:
        context = dict()

    return render(request , 'single-blog.html' , context)

def IndexPage(request):
    items = Blog.objects.all()
    bakhsh = Paginator(items , 4)
    page = request.GET.get("page")
    posts = bakhsh.get_page(page)

    context = {
        'posts':posts,
        'scat':EventCategory.objects.all(),
        'newest_b': items[:4],
        'admin_pic':HomeBack.objects.get(pk=1),
    }
    

    return render(request , "blog.html" , context)

@login_required
def AccessPage(request):
    if request.method == 'POST':
        EropStudent.objects.get_or_create(reason = request.POST.get('reason') ,
                                   come_from=request.user)
        
        context = {
            'access' : 'randomshit' , 
        }

        return render(request , 'wait.html' , context)
    else:
        return redirect('/')