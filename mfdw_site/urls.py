"""mfdw_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView
from quotes.views import Register

urlpatterns = [
    url(r'^testpage$', TemplateView.as_view(template_name="pages/page.html")),
    url(r'^admin/', admin.site.urls),
    url(r'^register/success/$', TemplateView.as_view(template_name="registration/success.html"), name ='register-success'),
    url('^register/$', Register.as_view(), name='register'),
    url(r'^quote', include('quotes.urls')),
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^bgpman', include('bgpman.urls')),
    url(r'^', include('pages.urls')),
]

# Change admin site title
admin.site.site_header = ("NOC Website Administration")
admin.site.site_title = ("NOC Site Admin")
