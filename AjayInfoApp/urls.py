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
    # urls for tally AMC
    path('tamc/', views.tamc, name='tamc'),
    # urls for tally corporate training 
    path('tctraining/', views.tctraining, name='tctraining'),
    # urls for tally customization
    path('tcustomization/', views.tcustomization, name='tcustomization'),
    # urls for tally synchronization
    path('tsynchronization/', views.tsynchronization, name='tsynchronization'),
    # urls for gallery
    path('gallery/', views.gallery, name='gallery'),
    # urls for blog details
    path('blogdetails/', views.blogdetails, name='blogdetails'),
    # urls for blog details 1
    path('blogdetails1/', views.blogdetails1, name='blogdetails'),
    # urls for blog details 2
    path('blogdetails2/', views.blogdetails2, name='blogdetails2'),
    # urls for gst services
    path('gstservice/', views.gstservice, name='gstservice'),
    # urls for gst filling
    path('gstfilling/', views.gstfilling, name='gstfilling'),
    # urls for inr filling
    path('inrfilling/', views.inrfilling, name='inrfilling'),
    # urls for data filling
    path('datafilling/', views.datafilling, name='datafilling'),
    # urls for tally prime 4.0 version
    path('downloadtp4', views.downloadtp4, name='downloadtp4'),
    # urls for tally prime edit log 4.0 version
    path('downloadtpel', views.downloadtpel4, name='downloadtpel4'),
    # urls for tally prime 3.0.1 version
    path('downloadtp301', views.downloadtp301, name='downloadtp301'),
    # urls for tally prime edit log 3.0.1 download urls
    path('downloadtpel301', views.downloadtpel301, name='downloadtpel301'),
    # urls for tally prime 3.0 version download
    path('downloadtp3', views.downloadtp3, name='downloadtp3'),
    # urls for tally prime edit log 3.0 version download
    path('downloadtpel3', views.downloadtpel3, name='downloadtpel3'),


    # other paths
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
