from django.db import models

# Create your models here.


class Bug(models.Model):
    bug_id = models.BigAutoField(primary_key=True, null=False)
    submitter_name = models.ForeignKey(
        'Submitter', on_delete=models.SET('none'))
    employee_id = models.ForeignKey('Employee', on_delete=models.SET('none'))
    description = models.TextField(null=False)
    completed = models.BooleanField()
    result_id = models.ForeignKey('Result', on_delete=models.PROTECT)
    created_at = models.DateField(
        'issue creation date', auto_now=True, null=False)
    modified_at = models.DateField()

    def __str__(self):
        return self.bug_id


class Submitter(models.Model):
    submitter_id = models.AutoField(primary_key=True, null=False)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    username = models.CharField(max_length=40)

    def __str__(self):
        return self.submitter_id


class Employee(models.Model):
    employee_id = models.AutoField(primary_key=True, null=False)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    username = models.CharField(max_length=40)

    def __str__(self):
        return "{0} {1}".format(self.employee_id, self.username)


class Discussion(models.Model):
    discussion_id = models.BigAutoField(primary_key=True, null=False)
    bug_id = models.ForeignKey('Bug', on_delete=models.PROTECT)
    message = models.TextField()
    created_at = models.DateField(auto_now=True, null=False)
    modified_at = models.DateField()

    def __str__(self):
        return self.discussion_id


class Result(models.Model):
    result_id = models.AutoField(primary_key=True, null=False)
    name = models.CharField(max_length=40)
    description = models.TextField()

    def __str__(self):
        return self.result_id