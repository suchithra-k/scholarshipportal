from django.db import models
from users.models import Organisation
from crawler.models import Scholarship


class OrganisationScholarship(models.Model):
    organisation = models.ForeignKey(Organisation, on_delete=models.CASCADE)
    scholarship = models.ForeignKey(Scholarship, on_delete=models.CASCADE)

    unique_together = ("organisation", "scholarship")
