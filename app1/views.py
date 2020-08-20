from django.shortcuts import render, redirect
from .models import Employee
from .forms import EmployeeForm

# Create your views here.
def insert_view(request):
    form = EmployeeForm()
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    return render(request, 'file/insert.html', {'form':form})

def show_view(request):
    employees = Employee.objects.all()
    return render(request, 'file/show.html', {'employees':employees})

def delete_view(request, Emp_ID):
    employees = Employee.objects.get(Emp_ID=Emp_ID)
    employees.delete()
    return redirect('/')

def update_view(request, Emp_ID):
    employees = Employee.objects.get(Emp_ID=Emp_ID)
    form = EmployeeForm(request.POST, instance=employees)
    if form.is_valid():
        form.save(commit=True)
        return redirect('/show')
    return render(request,'file/update.html', {'employees':employees})