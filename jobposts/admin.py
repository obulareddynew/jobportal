from django.contrib import admin
from .models import LatestJobs
from .models import TopRecruitersList
# Register your models here.
admin.site.register(LatestJobs)
admin.site.register(TopRecruitersList)