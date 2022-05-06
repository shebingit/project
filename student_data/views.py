from django.shortcuts import redirect, render
from django.contrib.auth.models import User,auth
from django.contrib import messages

from .models import *

def loginpage(request):
    return render(request,'login.html')  

def  home_page(request):
    return render(request,'welcome.html')

def home_page_load(request):
    courses=course_data.objects.all()
    course_id={'courses': courses}
   # print(course_id)
    return render(request,'student_add.html',course_id)


def login(request): 
    try:
        if request.method == 'POST':
            try:
                username = request.POST['username']
                password = request.POST['password']
                user = auth.authenticate(username=username, password=password)
                request.session["uid"] = user.id
                if user is not None:
                    auth.login(request, user)
                   # messages.info(request, f'Welcome {username}')
                    return redirect('home_page')
                else:
                    messages.info(request, 'Invalid username or password')
                    return redirect('loginpage')
            except:
                messages.info(request, 'Invalid username or password')
                return render(request, 'login.html')
        else:
            messages.info(request, 'Invalid username or password')
            return render(request, 'login.html')
    except:
        messages.info(request, 'Invalid username or password')
        return render(request, 'login.html')




#adding student data

def student_add(request):

    if request.method=="POST":
        name=request.POST['st_name']
        address=request.POST['st_address']
        age=request.POST['st_age']
        dob=request.POST['st_dob']
        cu_id=request.POST['c_id']
        course=course_data.objects.get(id=cu_id)

 #saving data

        stud=student_data(st_name=name,
                          st_address=address,
                          st_age=age,
                          st_dob=dob,
                          course_data=course)
        stud.save()
      

        courses=course_data.objects.all()
       
        #course_id={'courses': courses}
        #print(course_id)
        return render(request,'student_add.html',{'courses': courses})
        #print(course_id) 
    
 
# adding course details

def course_data_add(request):
    if request.method=="POST":
        cour_name=request.POST['cour_name']
        cour_fee=request.POST['cour_fee']
        cours=course_data(cu_name=cour_name,
        cu_fee=cour_fee,)

        cours.save()
        return redirect('course_data_add')
    return render(request,'course_add.html')
#load student course

def show_data(request):
    courses=student_data.objects.all()
    #course_id={'courses': courses}
    #print(course_id)
    return render(request,'data_show.html',{'courses': courses})    

def logout(request):
    request.session["uid"] = ""
    auth.logout(request)
    return redirect('loginpage')