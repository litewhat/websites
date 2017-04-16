from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.base import RedirectView
from django.views.generic.edit import CreateView

from celery import chain

from sites.models import Website
from sites import tasks

website_source = 'http://s3.amazonaws.com/alexa-static/top-1m.csv.zip'


class WebsiteListView(ListView):
    model = Website

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['field_names'] = [field.name
                                  for field in self.model._meta.fields]
        return context

    def get_queryset(self):
        if self.request.GET:
            category = self.request.GET['category']
            return Website.objects.filter(category__name=category)
        return Website.objects.all()


class WebsiteDetailView(DetailView):
    model = Website


class WebsiteCreateView(CreateView):
    model = Website
    fields = ['url', 'title', 'meta_description', 'alexa_rank', 'category']

    def get_success_url(self):
        pk = self.object.pk
        return reverse_lazy('sites:detail', kwargs={'pk': pk})


class GetWebsitesView(RedirectView):
    pattern_name = 'sites:list'

    def get_redirect_url(self, *args, **kwargs):
        task_queue = chain(
            tasks.get_file_from_url.s(website_source) |
            tasks.process_zipped_csv_file.s() |
            tasks.get_data_from_csv_file.s() |
            tasks.get_data_from_csv_file.s()
        )
        task_queue()
        return super().get_redirect_url(*args, **kwargs)

