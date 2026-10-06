# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Users(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(unique=True, max_length=100)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'


class Resumes(models.Model):
    user = models.ForeignKey(Users, models.DO_NOTHING)
    file_name = models.CharField(max_length=255)
    resume_text = models.TextField(blank=True, null=True)
    uploaded_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'resumes'


class Skills(models.Model):
    skill_name = models.CharField(unique=True, max_length=100)

    class Meta:
        managed = False
        db_table = 'skills'


class Jobs(models.Model):
    user = models.ForeignKey(Users, models.DO_NOTHING)
    job_title = models.CharField(max_length=255)
    job_description = models.TextField()
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jobs'


class ResumeSkills(models.Model):
    resume = models.ForeignKey(Resumes, models.DO_NOTHING)
    skill = models.ForeignKey(Skills, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'resume_skills'


class JobSkills(models.Model):
    job = models.ForeignKey(Jobs, models.DO_NOTHING)
    skill = models.ForeignKey(Skills, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'job_skills'
