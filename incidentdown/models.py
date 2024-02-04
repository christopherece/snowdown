from django.db import models
from datetime import datetime


# Create your models here.

class IncidentDown(models.Model):
    # IMPACT_TYPE = (
    #     ('1 - 4 Users','1 - 4 Users'),
    #     ('Multiple Users (5+)','Multiple Users (5+)'),
    #     ('Entire Department / Site','Entire Department / Site'),
    #     ('Entire Organization','Entire Organization'),
    # )

    # URGENCY_TYPE = (
    #     ('Impeding normal work','Impeding normal work'),
    #     ('Preventing non-urgent work','Preventing non-urgent work'),
    #     ('Preventing urgent work','Preventing urgent work'),
    #     ('Blocking critical business','Blocking critical business'),
    # )

    # STATE_TYPE = (
    #     ('New','New'),
    #     ('In Progress','In Progress'),
    #     ('On-Hold','On-Hold'),
    #     ('Resolved','Resolved'),
    #     ('Cancelled','Cancelled'),
    # )

    name = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=200, blank=True, null=True, db_column='emailAddress')
    description = models.TextField(blank=True, null=True, db_column='description')
    impact = models.CharField(max_length=200, default='1 - 4 Users')
    urgency = models.CharField(max_length=200, default='Impeding normal work')
    worknotes = models.TextField(blank=True, null=True)
    assignment_group = models.CharField(max_length=200,blank=True, null=True)
    state = models.CharField(max_length=200, default='New')
    date = models.DateTimeField(auto_now_add=True)
    process = models.BooleanField(default=False)

    class Meta:
        db_table = 'SNDownForm'
        ordering = ('date', )

    def __str__(self):
        return self.name
    


class SnowIncident(models.Model):

    name = models.CharField(max_length=200, blank=True, null=True, db_column='caller_id')
    email = models.EmailField(max_length=200, blank=True, null=True, db_column='emailAddress')
    comments = models.TextField(blank=True, null=True, db_column='comments')
    description = models.TextField(blank=True, null=True, db_column='description')
    impact = models.IntegerField(default=4)
    urgency = models.IntegerField(default=4)
    worknotes = models.TextField(blank=True, null=True)
    assignment_group = models.CharField(max_length=200,blank=True, null=True)
    state = models.IntegerField(default=1)
    date = models.DateTimeField(auto_now_add=True)
    process = models.BooleanField(default=False)

    class Meta:
        db_table = 'SnowIncidentForm'
        ordering = ('date', )

    def __str__(self):
        return self.name