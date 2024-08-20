from django.shortcuts import render
from django.http import HttpResponse, FileResponse
from django.conf import settings
import os

# Create your views here.

# Home view:
def home(request):
    return render(request, 'index.html')

# About view:
def about(request):
    return render(request, 'about.html')

# Services Page:
def services(request):
    return render(request, 'services.html')

# Blog view:
def blog(request):
    return render(request, 'blog.html')

# Contact view:
def contact(request):
    return render(request, 'contact.html')

# Products view:
def products(request):
    return render(request, 'products.html')

# Quotes view:
def quotes(request):
    return render(request, 'quotes.html')

# Details view:
def details(request):
    return render(request, 'details.html')

# Tally Prime view:
def tallyprime(request):
    return render(request, 'tallyprime.html')

# Download Page view:
def downloadpage(request):
    return render(request, 'downloadpage.html')

# Download for Tally Prime application:
def downloadtp(request):
    # Construct the file path relative to MEDIA_ROOT
    file_path = os.path.join(settings.MEDIA_ROOT, 'downloads', 'setup (2).exe')
    
    # Check if the file exists
    if os.path.exists(file_path):
        return FileResponse(open(file_path, 'rb'), as_attachment=True, filename='tallyprime.exe')
    else:
        return HttpResponse("File not found")


# Download for Tally Prime Edit Log
def downloadtpel(request):
    file_path = os.path.join(settings.MEDIA_ROOT, 'downloads', 'setup (4).exe')
    if os.path.exists(file_path):
        return FileResponse(open(file_path,'rb'), as_attachment=True, filename='tallyprimeeditlog.exe')
    else:
        return HttpResponse("File not found")
    

# Tally Prime Server view:
def tpserver(request):
    return render(request, 'tpserver.html')


# Tally On Mobile viewws
def tmobile(request):
    return render(request, 'tmobile.html')

# Tally On Cloud view:
def tcloud(request):
    return render(request, 'tcloud.html')

# Tally AMC view :
def tamc(request):
    return render(request, 'tamc.html')

# Tally Corporate Training view :
def tctraining(request):
    return render(request, 'tctraining.html')

# Tally Customization view :
def tcustomization(request):
    return render(request, 'tcustomization.html')

# Tally Synchronization views:
def tsynchronization(request):
    return render(request, 'tsynchronization.html')

# Gallery view:
def gallery(request):
    return render(request, 'gallery.html')

# blog de3tails view:
def blogdetails(request):
    return render(request, 'blogdetails.html')

# blog details 1 view:
def blogdetails1(request):
    return render(request, 'blogdetails1.html')

# blog details 2 view
def blogdetails2(request):
    return render(request, 'blogdetails2.html')