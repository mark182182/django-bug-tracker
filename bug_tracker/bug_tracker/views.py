from django.shortcuts import render
from django.http import JsonResponse
from bug_tracker.models import Employee
from bug_tracker.services.employee import EmployeeRepo
import random
import json
# Create your views here.


def employee_by_id(request):
    employee = EmployeeRepo.get_employee_by_id(
        json.loads(request.body)['employee_id'])
    return JsonResponse(employee)


def employees(request):
    return JsonResponse(dict(employees=list(EmployeeRepo.get_employees())))
