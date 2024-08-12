from django.shortcuts import render

# Create your views here.


# home view:

def home(Request):
    return render(Request, 'index.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def blog(request):
    return render(request, 'blog.html')

def contact(request):
    return render(request, 'contact.html')

def products(request):
    return render(request,'products.html')

def quotes(request):
    return render(request, 'quotes.html')