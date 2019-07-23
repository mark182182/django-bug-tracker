from django.db import models


class Bug(models.Model):
    bug_id = models.BigAutoField(primary_key=True, null=False)
    submitter_name = models.ForeignKey(
        'Submitter', on_delete=models.SET('none'))
    employee_id = models.ForeignKey(
        'Employee', on_delete=models.SET('none'), null=True)
    description = models.TextField(null=False)
    completed = models.BooleanField(default=False)
    result_id = models.ForeignKey(
        'Result', on_delete=models.PROTECT, default=1)
    created_at = models.DateField(
        'issue creation date', auto_now_add=True, null=False)
    modified_at = models.DateField(auto_now=True, null=True)

    def __str__(self):
        return self.bug_id


class Submitter(models.Model):
    first_name = models.CharField(max_length=200, null=False)
    last_name = models.CharField(max_length=200, null=False)
    username = models.CharField(max_length=40, null=False)

    def __str__(self):
        return self.username


class Employee(models.Model):
    first_name = models.CharField(max_length=200, null=False)
    last_name = models.CharField(max_length=200, null=False)
    username = models.CharField(max_length=40, null=False)

    def __str__(self):
        return "{0} {1}, {2}".format(self.first_name, self.last_name, self.username)


class Discussion(models.Model):
    discussion_id = models.BigAutoField(primary_key=True, null=False)
    bug_id = models.ForeignKey('Bug', on_delete=models.PROTECT, null=False)
    message = models.TextField(null=False)
    created_at = models.DateField(auto_now_add=True, null=False)
    modified_at = models.DateField(auto_now=True, null=True)

    def __str__(self):
        return self.discussion_id


class Result(models.Model):
    name = models.CharField(max_length=40, null=False)
    description = models.TextField(null=True)

    def __str__(self):
        return self.name
