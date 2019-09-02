from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from bug_tracker.repos.employee import EmployeeRepo
from bug_tracker.repos.submitter import SubmitterRepo
from bug_tracker.repos.bug import BugRepo
from bug_tracker.repos.discussion import DiscussionRepo
import json


def employee(request):
    if (request.method == "GET"):
        employee = EmployeeRepo.get_employee_by_id(
            json.loads(request.body)['employee_id'])
        return JsonResponse(employee)


def employees(request):
    if (request.method == "GET"):
        print(dict(employees=list(EmployeeRepo.get_employees())))
        return JsonResponse(dict(employees=(EmployeeRepo.get_employees())))


def submitter(request):
    if (request.method == "GET"):
        submitter = SubmitterRepo.get_submitter_instance_by_username(
            json.loads(request.body)['username'])
        return JsonResponse(submitter)


def bug(request):
    if (request.method == "GET"):
        bug = BugRepo.get_bug_by_id(json.loads(request.body)['bug_id'])
        return JsonResponse(bug)

    if (request.method == "POST"):
        BugRepo.create_bug(json.loads(request.body)['bug'])
        return HttpResponse(status=200)

    if (request.method == "DELETE"):
        BugRepo.delete_bug_by_id(json.loads(request.body)['bug_id'])
        return HttpResponse(status=200)

    if (request.method == "PUT"):
        BugRepo.update_bug_by_employee_id(json.loads(request.body)['bug'])
        return HttpResponse(status=200)


def bugs(request):
    if (request.method == "GET"):
        return JsonResponse(dict(bugs=(BugRepo.get_bugs())))


def bugs_by_submitter(request):
    if (request.method == "GET"):
        bugs = BugRepo.get_bugs_by_submitter(
            json.loads(request.body)['submitter_username'])
        return JsonResponse(dict(bugs=(bugs)))


def discussion(request):
    if (request.method == "POST"):
        DiscussionRepo.create_discussion_by_bug_id(
            json.loads(request.body)['discussion'])
        return HttpResponse(status=200)


def discussions(request):
    if (request.method == "GET"):
        return JsonResponse(dict(discussion=(DiscussionRepo.get_discussions_by_bug_id(json.loads(request.body)['bug_id']))))
