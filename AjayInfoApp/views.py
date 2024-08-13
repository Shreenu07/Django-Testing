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