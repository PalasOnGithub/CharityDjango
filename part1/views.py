from django.shortcuts import render , redirect
import random
from .models import HomeBack , StudentRegisteration
from part2.models import Blog , Studentprofolio , Track
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate , login , logout
from django.contrib import messages
from django.contrib.auth.models import User
import jdatetime
import os 

# Create your views here.

def IndexPage(request):
    main_pic4 = HomeBack.objects.get(num_page = 4)
    main_pic1 = HomeBack.objects.get(num_page = 1)

    new_News = Blog.objects.all()

    context = {
        'home_pic1':main_pic1,
        'home_pic4':main_pic4,
        'news':new_News,
    }
    return render(request , 'index.html' , context)

def ContactPage(request):
    return render(request , 'contact.html')

def SearchPage(request):
    return render(request , 'blog.html')

def LoginPage(request):
    if not request.user.is_authenticated:
        return render(request , 'login.html')
    else:
        return redirect('/dashboard-user/')

def LogCheck(request):
    if request.method == "POST" and 'login' in request.META['HTTP_REFERER'] and not request.user.is_authenticated:
        form_name = request.POST.get('username')
        form_pass = request.POST.get('password')
        user = authenticate(request , username=str(form_name), password=str(form_pass))
        if user is not None:
            login(request, user)
            return redirect("/dashboard-user")
        else:
            user = User.objects.create_user(username=form_name,
                                            password=form_pass)
            login(request, user)
            return redirect('/dashboard-user/')
        
    elif request.method == "POST" and 'register' in request.META['HTTP_REFERER'] and not request.user.is_authenticated:
        form_name = request.POST.get('username').lower()
        form_pass = request.POST.get('password')
        try:
            user = User.objects.create_user(username=form_name,
                                            password=form_pass)
            login(request, user)
            return redirect('/blog/')
        except:
            return redirect('/dashboard-user/')
    else:
        return redirect("/dashboard-user")



def RegistrationPage(request):
    if not request.user.is_authenticated:
        return render(request , 'signup.html')
    else:
        return redirect('/dashboard-user/')


def LogOutPage(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('/')
    
    else:
        return redirect('/')

@login_required
def DashBoardPage(request):
    items = list(Track.objects.all())
    Random_ahang = random.choice(items)

    try:
        student_inf = Studentprofolio.objects.get(from_user = request.user)
        
    except:
        student_inf = None

    context = {
		'random_ahang':Random_ahang,
        'infs':student_inf,
        
    }

    return render(request , 'profile.html', context)


@login_required
def RegisteringInformation(request):
    if not StudentRegisteration.objects.filter(from_user = request.user).last():
        if request.method == "POST":
            StudentRegisteration.objects.create( 
            stu_pic = request.FILES.get('file') ,
            stu_name = request.POST.get("stu_name") , 
            stu_lastname = request.POST.get("stu_lastname") , 
            stu_fathername = request.POST.get("stu_fathername") , 
            stu_birthdate = jdatetime.date(int(float(request.POST.get("stu_birthdate").split("-")[0])) , int(float(request.POST.get("stu_birthdate").split("-")[1])) , int(float(request.POST.get("stu_birthdate").split("-")[2]))) ,
            stu_joindate = jdatetime.date.today() , 
            stu_sex = request.POST.get("stu_sex") , 
            stu_par = request.POST.get("stu_par") , 
            stu_pos = request.POST.get("stu_pos") , 
            stu_major = request.POST.get("stu_major") , 
            stu_nationalcode = request.POST.get("stu_nationalcode") , 
            stu_intshenas = request.POST.get("stu_intshenas") , 
            stu_placerio = request.POST.get("stu_placerio") , 
            stu_placerig = request.POST.get("stu_placerig") , 
            stu_level = request.POST.get("stu_level") , 
            stu_avrage = request.POST.get("stu_avrage") , 
            stu_status = request.POST.get("stu_status") , 
            stu_dirschool = request.POST.get("stu_dirschool") , 
            stu_schoolcode = request.POST.get("stu_schoolcode") , 
            stu_lastlevel = request.POST.get("stu_lastlevel") , 
            stu_lastschool = request.POST.get("stu_lastschool") , 
            stu_lastavrage = request.POST.get("stu_lastavrage") , 
            stu_lastlowcourse = request.POST.get("stu_lastlowcourse") , 
            par_fullname = request.POST.get("par_fullname") , 
            par_courselevel = request.POST.get("par_courselevel") , 
            par_birthdate = jdatetime.date(int(float(request.POST.get("par_birthdate").split("-")[0])) , int(float(request.POST.get("par_birthdate").split("-")[1])) , int(float(request.POST.get("par_birthdate").split("-")[2]))) ,
            par_job = request.POST.get("par_job") , 
            par_jobloc = request.POST.get("par_jobloc") , 
            par_jobnum = request.POST.get("par_jobnum") , 
            fam_loc = request.POST.get("fam_loc") , 
            fam_staticnum = request.POST.get("fam_staticnum") , 
            fam_dynamicnum = request.POST.get("fam_dynamicnum") , 
            fam_locstatus = request.POST.get("fam_locstatus") , 
            fam_locdesc = request.POST.get("fam_locdesc") , 
            fam_numofiters = request.POST.get("fam_numofiters") , 
            from_user = request.user
            )

        return render(request , 'wait.html')
    else:
        return redirect('/dashboard-user')