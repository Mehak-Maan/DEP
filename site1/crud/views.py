from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from .models import Employee
from .forms import login_form
from django.contrib.auth import login,authenticate
# Create your views here.
from django.contrib.auth.decorators import login_required
@login_required
def home(request):
     employee=Employee.objects.all()
     
        
         
     return render(request,"crud/main.html",{"employee":employee})

def create(request):
    if request.method =="POST":
      first=request.POST.get("firstname",None)
      last=request.POST.get("lastname",None)
      new=Employee(firstname=first,lastname=last)
      new.save()

      return redirect("home")
    return render(request,"crud/create.html",)
def delete(request,e_id):
    employee=get_object_or_404(Employee,id=e_id)
    employee.delete()
    print(e_id)
    return redirect("/crud/home")
def update(request,e_id):
    
    employee=get_object_or_404(Employee,id=e_id)
    if request.method=="POST":
         first=request.POST.get("firstname",None)
         last=request.POST.get("lastname",None)
         job=request.POST.get("job",None)
         update_employee=Employee.objects.get(id=e_id)
         update_employee.firstname=first
         update_employee.lastname=last
         update_employee.job=job
         update_employee.save()
         return redirect("/crud/home")
    return render(request,"crud/update.html",{"employee":employee})
def user_login(request):
    if request.method == "POST":
         username=request.POST.get("username",None)
         password=request.POST.get("password",None)
         user=authenticate(username=username,password=password)
         print(user)
             
         if user is not None:
           
             login(request,user)
             
             return render(request,"crud/home.html")
         else:
             return render(request,"crud/login.html",{"error":"Username or Password is not correct "})
    else:
         #return redirect('home')
    
        
        
      #return render(request,"crud/login.html",{"form":form})
        return render(request,"crud/login.html",)
    