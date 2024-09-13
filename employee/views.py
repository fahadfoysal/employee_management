from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.db.models import Q
from .models import Employee
from .forms import EmployeeForm

def employee_list(request):
    return render(request, 'employee/employee_list.html')

def employee_data(request):
    name_filter = request.GET.get('name', '')
    dob_filter = request.GET.get('dob', '')
    email_filter = request.GET.get('email', '')
    mobile_filter = request.GET.get('mobile', '')

    employees = Employee.objects.all()

    if name_filter:
        words = name_filter.split()
        if len(words) == 1:
            employees = employees.filter(Q(first_name__icontains=words[0]) | Q(last_name__icontains=words[0]))

        elif len(words) >= 2:
            employees = employees.filter(
                Q(first_name__icontains=words[0]) & Q(last_name__icontains=words[1]) |
                Q(first_name__icontains=words[1]) & Q(last_name__icontains=words[0])
            )

    if email_filter:
        employees = employees.filter(email__icontains=email_filter)

    if dob_filter:
        employees = employees.filter(date_of_birth=dob_filter)

    if mobile_filter:
        employees = employees.filter(mobile__icontains=mobile_filter)

    # processing data to passing to the data table
    data = []
    for employee in employees:
        data.append({
            'id': employee.id,
            'photo': f'<img src="{employee.photo.url}" class="employee-photo" alt="Employee Photo">' if employee.photo else '',
            'full_name': employee.full_name,
            'email': employee.email,
            'mobile': employee.mobile,
            'date_of_birth': employee.date_of_birth.strftime('%Y-%m-%d'),
            'actions': f'''
                <button class="edit-button" data-id="{employee.id}">
                    <i class="fas fa-edit"></i>
                </button> 
                <button class="delete-button" data-id="{employee.id}">
                    <i class="fas fa-trash-alt"></i>
                </button>
            ''',
        })

    return JsonResponse({'data': data})

def employee_delete(request, pk):
    if request.method == 'POST':
        employee = get_object_or_404(Employee, pk=pk)
        employee.delete()
        return JsonResponse({'success': True, 'message': 'Employee deleted successfully!'})

    return JsonResponse({'success': False, 'message': 'Invalid request method.'})

def employee_update(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'employee/employee_update.html', {'form': form})

def employee_add(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm()
    return render(request, 'employee/employee_add.html', {'form': form})
        
