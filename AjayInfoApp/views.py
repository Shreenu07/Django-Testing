from django.shortcuts import render
from django.http import HttpResponse, FileResponse, Http404
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

# gst services views:
def gstservice(request):
    return render(request, 'gstservice.html')

# gst filling views:
def gstfilling(request):
    return render(request, 'gstfilling.html')

# inr filling views:
def inrfilling(request):
    return render(request, 'inrfilling.html')

# data filling views:
def datafilling(request):
    return render(request, 'datafilling.html')

# download tally prime version 4.0
def downloadtp4(request):
    file_path = os.path.join(settings.MEDIA_ROOT, 'downloads', 'tallyprime4.exe')
    if os.path.exists(file_path):
        try:
            return FileResponse(open(file_path, 'rb'), as_attachment=True, filename='tallyprimeversion4.exe')
        except Exception as e:
            # Optionally log the exception
            return HttpResponse(f"An error occurred while processing your request: {str(e)}")
    else:
        raise Http404("File not found")


# download tally prime version edit log 4.0 views
def downloadtpel4(request):
    file_path = os.path.join(settings.MEDIA_ROOT, 'downloads', 'tallyprimeelg4.exe')
    if os.path.exists(file_path):
        return FileResponse(open(file_path, 'rb'), as_attachment=True, filename='tallyprimeeditlog4.exe')
    else:
        return HttpResponse("File not found")


# download tally prime 3.0.1 version views
def downloadtp301(request):
    file_path = os.path.join(settings.MEDIA_ROOT, 'downloads', 'tallyprime301.exe')
    if os.path.exists(file_path):
        return FileResponse(open(file_path, 'rb'), as_attachment=True, filename='tallyprime301.exe')
    else:
        return HttpResponse('File not found')
    

# download tally prime edit log 3.0.1 version view
def downloadtpel301(request):
    file_path = os.path.join(settings.MEDIA_ROOT, 'downloads', 'tallyprimeeditlog301.exe')
    if os.path.exists(file_path):
        return FileResponse(open(file_path , 'rb'), as_attachment=True, filename='tallyprimeeditlog301.exe')
    else:
        return HttpResponse("File not found")
    
# download tally prime 3.0 version view
def downloadtp3(request):
    file_path = os.path.join(settings.MEDIA_ROOT, 'downloads', 'tallyprime3.exe')
    if os.path.exists(file_path):
        return FileResponse(open(file_path, 'rb'), as_attachment=True, filename='tallyprime3.exe')
    else:
        return HttpResponse("File not found")
    
# download tally prime 3.0 version view
def downloadtpel3(request):
    file_path = os.path.join(settings.MEDIA_ROOT, 'downloads', 'tallyprimeeditlog3.exe')
    if os.path.exists(file_path):
        return FileResponse(open(file_path, 'rb'), as_attachment=True, filename='tallyprimeeditlog3.exe')
    else:
        return HttpResponse("File not found")
    

# download tally prime 2.1 view
def downloadtp21(request):
    file_path = os.path.join(settings.MEDIA_ROOT, 'downloads', 'tallyprime21.exe')
    if os.path.exists(file_path):
        return FileResponse(open(file_path, 'rb'), as_attachment=True, filename='tallyprime21.exe')
    else:
        return HttpResponse("File not found")
    

# download tally prime edit log 2.1 views
def downloadtpel21(request):
    file_path = os.path.join(settings.MEDIA_ROOT, 'downloads', 'tallyprimeeditlog21.exe')
    if os.path.exists(file_path):
        return FileResponse(open(file_path, 'rb'), as_attachment=True, filename="tallyprimeeditlog21.exe")
    else:
        return HttpResponse("File not found")
    

# downlaod tally prime 2.0.1 views
def downloadtp201(request):
    file_path = os.path.join(settings.MEDIA_ROOT, 'downloads', 'tallyprime201.exe')
    if os.path.exists(file_path):
        return FileResponse(open(file_path, 'rb'), as_attachment=True, filename='tallyprime201.exe')
    else:
        return HttpResponse("File not found")
    
# download tally prime 2.0 view
def downloadtp2(request):
    file_path = os.path.join(settings.MEDIA_ROOT, 'downloads', 'tallyprime2.exe')
    if os.path.exists(file_path):
        return FileResponse(open(file_path, 'rb'), as_attachment=True, filename='tallyprime2.exe')
    else:
        return HttpResponse("File not found")
    


# download tally prime 1.1.4 views
def downloadtp114(request):
    file_path = os.path.join(settings.MEDIA_ROOT, 'downloads', 'tallyprime114.exe')
    if os.path.exists(file_path):
        return FileResponse(open(file_path, 'rb'), as_attachment=True, filename='tallyprime114.exe')
    else:
        return HttpResponse("File not found")
    


# download tally prime 1.1.3 views
def downloadtp113(request):
    file_path = os.path.join(settings.MEDIA_ROOT, 'downloads', 'tallyprime113.exe')
    if os.path.exists(file_path):
        return FileResponse(open(file_path, 'rb'), as_attachment=True, filename='tallyprime113.exe')
    else:
        return HttpResponse("File not found")
    
# download tally prime 1.1.2 views
def downloadtp112(reuqest):
    file_path = os.path.join(settings.MEDIA_ROOT, 'downloads', 'tallyprime112.exe')
    if os.path.exists(file_path):
        return FileResponse(open(file_path, 'rb'), as_attachment=True, filename='tallyprime112.exe')
    else:
        return HttpResponse("File not found")
    


# download tally prime 1.1.1 view
def downloadtp111(request):
    file_path = os.path.join(settings.MEDIA_ROOT, 'downloads', 'tallyprime111.exe')
    if os.path.exists(file_path):
        return FileResponse(open(file_path, 'rb'), as_attachment=True, filename='tallyprime111.exe')
    else:
        return HttpResponse("File not found")
    


# career page view
def career_page(request):
    return render(request, 'career.html')


# testimononials page vew
def testimonials(request):
    return render(request, 'testimonials.html')