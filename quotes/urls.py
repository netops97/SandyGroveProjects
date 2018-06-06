from django.conf.urls import url

from . import views
from .views import QuoteList, QuoteView

urlpatterns = [
    url(r'^$', views.quote_req, name='quote-request'),
    url(r'show/(?P<pk>[0-9]+)$', QuoteView.as_view(), name='quote-detail'),
    url(r'show$', QuoteList.as_view(), name='show-quotes'),
]
