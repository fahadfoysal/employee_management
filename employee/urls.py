from django.urls import path
from .views import employee_list, employee_data, employee_update, employee_delete, employee_add

urlpatterns = [
    path('', employee_list, name='employee_list'),
    path('employees/', employee_data, name='employee_data'),
    path('employees/add/', employee_add, name='employee_add'),
    path('employees/update/<int:pk>/', employee_update, name='employee_update'),
    path('employees/delete/<int:pk>/', employee_delete, name='employee_delete'),
]
