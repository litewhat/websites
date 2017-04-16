from django.db import models
from django.urls import reverse


class Website(models.Model):
    url = models.URLField(
        unique=True,
        verbose_name='url',
    )
    title = models.CharField(
        verbose_name='title',
        max_length=100,
    )
    meta_description = models.TextField()
    alexa_rank = models.IntegerField()
    category = models.ForeignKey(
        'categories.WebsiteCategory',
        on_delete=models.CASCADE,
        verbose_name='category',
    )
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('sites:detail', kwargs={'pk': self.pk})


class WebPage(models.Model):
    url = models.URLField(
        unique=True,
        verbose_name='url',
    )
    title = models.CharField(
        verbose_name='title',
        max_length=100,
    )
    website = models.ForeignKey(
        'Website',
        verbose_name='website',
        on_delete=models.CASCADE
    )
    meta_description = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
