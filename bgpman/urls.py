from django.conf.urls import url

from . import views
#from .views import RouterList

urlpatterns = [
    url(r'^$', views.router_req, name='router-request'),
    #url(r'show$', routerList.as_view(), name='show-routers'),
]
