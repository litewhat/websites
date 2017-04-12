from django.conf.urls import url
from .views import WebsiteListView, WebsiteDetailView, WebsiteCreateView

urlpatterns = [
    url(r'^$', WebsiteListView.as_view(), name='list'),
    url(r'^(?P<pk>[0-9]+)/$', WebsiteDetailView.as_view(), name='detail'),
    url(r'^create/$', WebsiteCreateView.as_view(), name='create'),
]
