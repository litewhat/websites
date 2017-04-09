from categories.models import WebsiteCategory
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView


class WebsiteCategoryListView(ListView):
    model = WebsiteCategory


class WebsiteCategoryCreateView(CreateView):
    model = WebsiteCategory
    fields = ['name', 'description']
    success_url = reverse_lazy('categories:list')

    def form_valid(self, form):
        form.instance.count = 0
        return super().form_valid(form)
