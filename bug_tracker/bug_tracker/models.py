from django.db import models

# Create your models here.


class Bug(models.Model):
    bug_id = models.BigAutoField(primary_key=True)
    submitter_name = models.ForeignKey(
        'Submitter', on_delete=models.SET('none'))
    employee_id = models.ForeignKey('Employee', on_delete=models.SET('none'))
    description = models.TextField()
    completed = models.BooleanField()
    result_id = models.ForeignKey('Result', on_delete=models.PROTECT)
    created_at = models.DateField('issue creation date', auto_now=True)
    modified_at = models.DateField()


class Submitter(models.Model):
    submitter_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    username = models.CharField(max_length=40)


class Employee(models.Model):
    employee_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    username = models.CharField(max_length=40)


class Discussion(models.Model):
    discussion_id = models.BigAutoField(primary_key=True)
    bug_id = models.ForeignKey('Bug', on_delete=models.PROTECT)
    message = models.TextField()
    created_at = models.DateField()
    modified_at = models.DateField()


class Result(models.Model):
    result_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=40)
    description = models.TextField()
