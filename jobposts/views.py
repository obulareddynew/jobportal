from django.shortcuts import render
from .models import LatestJobs
from .models import TopRecruitersList
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
# Create your views here.
def index(request):
    jobs1=LatestJobs.objects.filter().order_by('-id')[:5]
    toprec=TopRecruitersList.objects.all()

    return render(request,'index.html',{'jobs1':jobs1,'toprec':toprec})
def contact(request):
    return render(request,"contact.html")
@login_required(login_url="login")
def alljobs(request):
    if ('slocation' in request.GET):
        loc=request.GET['slocation']
        skil=request.GET['sskill']
        comp=request.GET['scompany']
    if ('slocation' in request.GET) and len(loc)>0 and len(comp)>0 and len(skil)>0:
        slocation=request.GET['slocation']
        jobs1=LatestJobs.objects.filter(location__icontains=slocation,companyname__icontains=comp,skills__icontains=skil)
    elif ('scompany' in request.GET) and len(loc)>0 and len(comp)>0:
        jobs1 = LatestJobs.objects.filter(location__icontains=loc, companyname__icontains=comp)
    elif ('sskill' in request.GET) and len(loc)>0 and len(skil)>0:
        jobs1 = LatestJobs.objects.filter(location__icontains=loc, skills__icontains=skil)
    elif ('sskill' in request.GET) and len(comp)>0 and len(skil)>0:
        jobs1 = LatestJobs.objects.filter( companyname__icontains=comp, skills__icontains=skil)
    elif ('scompany' in request.GET) and len(loc)>0:
        jobs1 = LatestJobs.objects.filter(location__icontains=loc)
    elif ('sskill' in request.GET) and len(comp) > 0:
        jobs1 = LatestJobs.objects.filter(companyname__icontains=comp)
    elif ('sskill' in request.GET) and len(skil) > 0:
        jobs1 = LatestJobs.objects.filter(skills__icontains=skil)
    else:
        jobs1 = LatestJobs.objects.all()
    return render(request,"alljobs.html",{'jobs1':jobs1})