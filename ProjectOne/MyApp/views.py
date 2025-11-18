from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .forms import studentForm,customUser
from . models import addStudent

# Create your views here.

#user registration function
def userRegistration(request):
    if request.method=="POST":
        form=customUser(request.POST)
        if form.is_valid():
            form.save()
            return redirect('fetchstd')
    else:
        form=customUser()
        context={'form':form}
        return render(request,"MyApp/user-regist.html",context)
    
# user login view
def login_view(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username, password=password)

        if user is not None:
            login(request,user)
            return redirect('fetchstd')
        
    
    return render(request,"MyApp/signin.html")
# user logout view
def logout_view(request):
    logout(request)
    return redirect('signin')




def Home(request):  
    return render(request, 'MyApp/landing_page.html')

def Stud(request):
    if request.method=='POST':
        form=studentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    
    else:
        form=studentForm()
        context={'form':form}
    return render(request, 'MyApp/studForm.html',context)    


def registerStd(request):
    if request.method=="POST":
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        regNo=request.POST['regNo']

        std=addStudent(first_name=fname, last_name=lname, std_email=email, std_regNo=regNo)
        # std.full_clean()
        std.save()
        return redirect('fetchstd')
    else:
        return render(request,'MyApp/add_std.html')

def fetchStd(request):
    data=addStudent.objects.all()
    context={'data':data}
    return render(request,'MyApp/std_detail.html',context)


def updateStd(request,pk):
    stud=get_object_or_404(addStudent,pk=pk)
    if request.method=='POST':
        new_fname=request.POST.get('fname')
        new_lname=request.POST.get('lname')
        new_email=request.POST.get('email')
        new_regNo=request.POST.get('regNo')

        stud.first_name=new_fname
        stud.last_name=new_lname
        stud.std_email=new_email
        stud.std_regNo=new_regNo

        stud.save()
        return redirect('fetchstd')

    else:
        context={'std':stud}
        return render(request, 'MyApp/updatestd.html',context)
    
def deleteStd(request,pk):
    delStd=get_object_or_404(addStudent,pk=pk)
    if request.method=='POST':
        delStd.delete()
        return redirect('fetchstd')
    
    else:
        context={'delStd':delStd}
    return render(request,'MyApp/deletestd.html',context)