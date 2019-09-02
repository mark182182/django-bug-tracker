from bug_tracker.models import Submitter
from bug_tracker.repos.util import UtilRepo


class SubmitterRepo:
    def get_submitter_instance_by_username(username):
        return UtilRepo.return_if_exists(Submitter.objects.filter(username=username))