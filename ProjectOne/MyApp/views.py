from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import studentForm
from . models import addStudent

# Create your views here.
def Home(request):
    return render(request, 'MyApp/menubar.html')

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
        return HttpResponse('data saved successfully')
    else:
        return render(request,'MyApp/index.html')
