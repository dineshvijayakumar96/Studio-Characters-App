from django.urls import path, include
from django.views.generic import RedirectView
from django.shortcuts import redirect
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('service-brand-identity', views.servicebrandidentity, name="servicebrandidentity"),
    path('service-website-design', views.servicewebsitedesign, name="servicewebsitedesign"),
    path('portfolio/evasion-exotique', views.evasionexotique, name="evasionexotique"),
    path('portfolio/enhance', views.enhance, name="enhance"),
    path('portfolio/antaracares', views.antaracares, name="antaracares"),
    path('portfolio/iconic-city', views.iconiccity, name="iconiccity"),
    path('portfolio/i2c2', views.i2c2, name="i2c2"),
    path('portfolio/edubest-online', views.edubestonline, name="edubestonline"),
    path('thank-you', views.thankyou, name="thankyou"),
    # Redirect patterns without trailing slashes to URLs with trailing slashes
    path('service-brand-identity/', RedirectView.as_view(url='/service-brand-identity', permanent=True)),
    path('service-website-design/', RedirectView.as_view(url='/service-website-design', permanent=True)),
    path('portfolio/', RedirectView.as_view(url='/', permanent=True)),
    path('portfolio', RedirectView.as_view(url='/', permanent=True)),
    path('portfolio/evasion-exotique/', RedirectView.as_view(url='/portfolio/evasion-exotique', permanent=True)),
    path('portfolio/enhance/', RedirectView.as_view(url='/portfolio/enhance', permanent=True)),
    path('portfolio/antaracares/', RedirectView.as_view(url='/portfolio/antaracares', permanent=True)),
    path('portfolio/iconic-city/', RedirectView.as_view(url='/portfolio/iconic-city', permanent=True)),
    path('portfolio/i2c2/', RedirectView.as_view(url='/portfolio/i2c2', permanent=True)),
    path('portfolio/edubest-online/', RedirectView.as_view(url='/portfolio/edubest-online', permanent=True)),
]