from bug_tracker.models import Result
from bug_tracker.repos.util import UtilRepo


class ResultRepo:

    def get_result_by_id(result_id):
        return Result.objects.filter(id=result_id)