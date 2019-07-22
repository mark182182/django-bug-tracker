from bug_tracker.models import Employee
# Create your views here.


def return_if_exists(queryset):
    if (queryset.exists()):
        return queryset.values()[0]
    else:
        return {"QuerySet": None}


class EmployeeRepo:
    def get_employee_by_id(employee_id):
        return return_if_exists(Employee.objects.filter(employee_id=employee_id))
