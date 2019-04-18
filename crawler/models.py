from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.db.models import Q


class ScholarshipManager(models.Manager):
    def filter_with_eligibility(self, marks=None, year=None, caste=None):
        query = Q()
        if marks is not None:
            query.add(Q(scholarshipeligibility__min_marks__lte=marks), Q.AND)

        if year is not None and year != '0':
            query.add(Q(scholarshipeligibility__year__contains=[year]), Q.AND)

        if caste is not None and caste != '':
            query.add(
                Q(scholarshipeligibility__caste__contains=[caste]), Q.AND)

        return super().get_queryset().filter(query)


class Scholarship(models.Model):
    title = models.CharField(max_length=500)
    slug = models.SlugField(max_length=500, unique=True)
    url = models.TextField()
    expiry_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ScholarshipManager()


class SchedulerAudit(models.Model):
    task = models.CharField(max_length=100)
    last_runtime = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField()
    remarks = models.TextField()


class ScholarshipEligibility(models.Model):
    scholarship = models.OneToOneField(
        Scholarship, on_delete=models.CASCADE)
    min_marks = models.FloatField(null=True)
    year = ArrayField(models.IntegerField(), null=True)
    caste = ArrayField(models.CharField(max_length=20), null=True)
