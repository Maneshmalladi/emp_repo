from django.shortcuts import render,redirect

# Create your views here.
from testapp.models import Employee
def retrieve_view(request):
    emp_list = Employee.objects.all()
    return render(request,'testapp/index.html',{'emp_list':emp_list})


from testapp.forms import EmployeeForm
def insert_view(request):
    form = EmployeeForm()
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    return render(request,'testapp/insert.html',{'form':form})



def delete_view(request,id):
    employee=Employee.objects.get(id=id)
    employee.delete()
    return redirect('/')


def update_view(request,id):
    employee=Employee.objects.get(id=id)
    form=EmployeeForm(instance=employee)
    if request.method=='POST':
        form=EmployeeForm(request.POST,instance=employee)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request,'testapp/update.html',{'form':form})
