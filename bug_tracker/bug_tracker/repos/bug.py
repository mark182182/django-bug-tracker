from bug_tracker.models import Bug
from bug_tracker.repos.util import UtilRepo
from bug_tracker.repos.submitter import SubmitterRepo


class BugRepo():
    def get_bug_by_id(bug_id):
        return UtilRepo.return_if_exists(Bug.objects.filter(bug_id=bug_id))

    def get_bug_instance_by_id(bug_id):
        return Bug.objects.filter(bug_id=bug_id)[0]

    def get_bugs_by_submitter(submitter_username):
        submitter = SubmitterRepo.get_submitter_instance_by_username(
            submitter_username)
        if ('QuerySet' in submitter):
            return submitter
        else:
            return UtilRepo.return_if_exists(Bug.objects.filter(submitter=submitter['id']))

    def get_bugs():
        return UtilRepo.return_if_exists(Bug.objects.all())

    def create_bug(bug):
        submitter=SubmitterRepo.get_submitter_instance_by_username(
            bug['submitter_name'])
        Bug.objects.create(submitter=submitter,
                           description=bug['description'])

    def delete_bug_by_id(bug_id):
        Bug.objects.filter(bug_id=bug_id).delete()

    def update_bug_by_employee_id(bug):
        Bug.objects.filter(bug_id=bug['bug_id']).update(
            employee=bug['employee_id'])

    def update_bug_by_result_id(bug):
        Bug.objects.filter(bug_id=bug['bug_id']).update(
            result=['result_id'])
