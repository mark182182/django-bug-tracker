from bug_tracker.models import Discussion
from bug_tracker.repos.util import UtilRepo
from bug_tracker.repos.bug import BugRepo


class DiscussionRepo:

    def get_discussions_by_bug_id(bug_id):
        return UtilRepo.return_if_exists(Discussion.objects.filter(bug_id=bug_id))

    def create_discussion_by_bug_id(discussion):
        bug = BugRepo.get_bug_instance_by_id(discussion['bug_id'])
        Discussion.objects.create(
            sender_username=discussion['username'], message=discussion['message'], bug_id=bug)
