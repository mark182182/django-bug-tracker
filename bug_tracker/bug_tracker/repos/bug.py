from bug_tracker.models import Bug
from bug_tracker.repos.util import UtilRepo
from bug_tracker.repos.submitter import SubmitterRepo

# bug_id = models.BigAutoField(primary_key=True, null=False)
# submitter_name = models.ForeignKey(
#     'Submitter', on_delete=models.SET('none'))
# employee_id = models.ForeignKey(
#     'Employee', on_delete=models.SET('none'), null=True)
# description = models.TextField(null=False)
# completed = models.BooleanField(default=False)
# result_id = models.ForeignKey(
#     'Result', on_delete=models.PROTECT, default=1)
# created_at = models.DateField(
#     'issue creation date', auto_now_add=True, null=False)
# modified_at = models.DateField(auto_now=True, null=True)


class BugRepo():
    def get_bug_by_id(bug_id):
        return UtilRepo.return_if_exists(Bug.objects.filter(bug_id=bug_id))

    def get_bugs():
        return UtilRepo.return_if_exists(Bug.objects.all())

    def create_bug(bug):
        submitter = SubmitterRepo.get_submitter_instance_by_username(
            bug['submitter_name'])
        Bug.objects.create(submitter_name=submitter,
                           description=bug['description'])

    def delete_bug_by_id(bug_id):
        Bug.objects.filter(bug_id=bug_id).delete()

    def update_bug_by_employee_id(bug):
        Bug.objects.filter(bug_id=bug['bug_id']).update(
            employee_id=bug['employee_id'])
