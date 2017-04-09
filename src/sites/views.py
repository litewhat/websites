from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from .models import Website


class WebsiteListView(ListView):
    model = Website


class WebsiteDetailView(DetailView):
    model = Website


class WebsiteCreateView(CreateView):
    model = Website
    fields = ['url', 'title', 'meta_description', 'alexa_rank', 'category']

    def get_success_url(self):
        pk = self.object.pk
        return reverse_lazy('sites:detail', kwargs={'pk': pk})
