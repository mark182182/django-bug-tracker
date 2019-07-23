from bug_tracker.models import Employee
from bug_tracker.repos.util import UtilRepo


class EmployeeRepo:
    def get_employee_by_id(employee_id):
        return UtilRepo.return_if_exists(Employee.objects.filter(id=employee_id))

    def get_employees():
        return UtilRepo.return_if_exists(Employee.objects.all())
