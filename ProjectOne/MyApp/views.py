from django.shortcuts import render,redirect
from .forms import studentForm

# Create your views here.
def Home(request):
    return render(request, 'MyApp/index.html')

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