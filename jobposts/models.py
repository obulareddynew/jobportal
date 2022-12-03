from django.db import models

# Create your models here.
class LatestJobs(models.Model):
    jobtitle=models.TextField()
    companyname=models.TextField()
    yearsofexp=models.TextField()
    location=models.TextField()
    JobDescp=models.TextField()
    salary=models.TextField()
    skills=models.TextField()

class TopRecruitersList(models.Model):
    comlogo=models.ImageField(upload_to='pics')


