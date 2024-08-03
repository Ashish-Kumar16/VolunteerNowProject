from django.db import models

class Organization(models.Model):
    name = models.CharField(max_length=255)
    about = models.TextField()

    def __str__(self):
        return self.name

class VolunteerOpportunity(models.Model):
    title = models.CharField(max_length=255)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    description = models.TextField()
    is_remote = models.BooleanField(default=False)
    location = models.CharField(max_length=255, null=True, blank=True)

class Application(models.Model):
    opportunity = models.ForeignKey(VolunteerOpportunity, on_delete=models.CASCADE)
    applicant_name = models.CharField(max_length=255)
    applicant_email = models.EmailField()

class Donation(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    donor_name = models.CharField(max_length=255)
    donor_email = models.EmailField()
