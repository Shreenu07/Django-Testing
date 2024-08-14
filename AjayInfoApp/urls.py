"""
URL configuration for AjayInfoProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    # urls for home/index page
    path('', views.home, name='home'),
    # urls for about page
    path('about/', views.about, name='about'),
    # urls for services page
    path('services/', views.services, name='services'),
    # urls for blog page
    path('blog/', views.blog, name='blog'),
    # urls for contact page
    path('contact/', views.contact, name='contact'),
    # urls for products page
    path('products/', views.products, name='products'),
    # urls for quotes page
    path('quotes/', views.quotes, name='quotes'),
    # urls for details page
    path('details/', views.details, name='details'),
    # urls for tally prime page
    path('tallyprime/', views.tallyprime, name='tallyprime'),
    # urls for download page
    path('downloadpage/',views.downloadpage, name='downloadpage'),
    # urls for download tally prime setup application
    path('downloadtp/', views.downloadtp, name='downloadtp'),
    # urls for download tally prime edit log application
    path('downloadtpel/', views.downloadtpel, name='downloadtpel'),
    # urls for tally prime server
    path('tpserver/', views.tpserver, name='tpserver'),
    # urls for tally on mobile
    path('tmobile/', views.tmobile, name='tmobile'),
    # urls for tally on cloud
    path('tcloud/', views.tcloud, name='tcloud'),

    # other paths
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
