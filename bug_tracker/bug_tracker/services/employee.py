from bug_tracker.models import Employee

def return_if_exists(queryset):
    if (queryset.exists()):
        if (len(queryset.values()) > 1):
            return list(queryset.values())
        else:
            return queryset.values()[0]
    else:
        return {"QuerySet": None}


class EmployeeRepo:
    def get_employee_by_id(employee_id):
        return return_if_exists(Employee.objects.filter(employee_id=employee_id))

    def get_employees():
        return return_if_exists(Employee.objects.all())
