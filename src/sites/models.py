from django.db import models


class Website(models.Model):
    url = models.URLField()
    title = models.CharField(max_length=100)
    meta_description = models.TextField()
    alexa_rank = models.IntegerField()
    category = models.ForeignKey(
        'categories.WebsiteCategory',
        on_delete=models.CASCADE,
    )
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('websites:detail', kwargs={'pk': self.pk})


class WebPage(models.Model):
    title = models.CharField(max_length=100)
    url = models.URLField(unique=True)
    website = models.ForeignKey(
        'Website',
        on_delete=models.CASCADE
    )
    meta_description = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
