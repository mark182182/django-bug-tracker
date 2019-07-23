from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from bug_tracker.repos.employee import EmployeeRepo
from bug_tracker.repos.bug import BugRepo
import json


def employee(request):
    if (request.method == "GET"):
        employee = EmployeeRepo.get_employee_by_id(
            json.loads(request.body))['employee_id']
        return JsonResponse(employee)


def employees(request):
    if (request.method == "GET"):
        return JsonResponse(dict(employees=list(EmployeeRepo.get_employees())))


def bug(request):
    if (request.method == "GET"):
        bug = BugRepo.get_bug_by_id(json.loads((request.body))['bug_id'])
        return JsonResponse(bug)

    if (request.method == "POST"):
        BugRepo.create_bug(json.loads((request.body))['bug'])
        return HttpResponse(status=200)

    if (request.method == "DELETE"):
        BugRepo.delete_bug_by_id(json.loads((request.body))['bug_id'])
        return HttpResponse(status=200)

    if (request.method == "PUT"):
        BugRepo.update_bug_by_employee_id(json.loads((request.body))['bug'])
        return HttpResponse(status=200)


def bugs(request):
    if (request.method == "GET"):
        return JsonResponse(dict(bugs=list(BugRepo.get_bugs())))
