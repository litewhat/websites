from django.conf.urls import url
from categories.views import WebsiteCategoryListView, WebsiteCategoryCreateView

urlpatterns = [
    url(r'^$', WebsiteCategoryListView.as_view(), name='list'),
    url(r'^create/$', WebsiteCategoryCreateView.as_view(), name='create'),
]