from django.shortcuts import render

# Create your views here.


# home view:

def home(Request):
    return render(Request, 'index.html')


# about view
def about(request):
    return render(request, 'about.html')


# Services Page
def services(request):
    return render(request, 'services.html')


# blog view
def blog(request):
    return render(request, 'blog.html')


# contact view
def contact(request):
    return render(request, 'contact.html')


# products view
def products(request):
    return render(request,'products.html')


# quotes view: 
def quotes(request):
    return render(request, 'quotes.html')


# details view
def details(request):
    return render(request, 'details.html')

# tally prime views:

def tallyprime(request):
    return render(request, 'tallyprime.html')