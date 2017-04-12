from django.test import TestCase
from django.test import Client
from django.urls import reverse, resolve
from sites.models import WebPage, Website
from categories.models import WebsiteCategory


class SavingNewObjectsTestCase(TestCase):

    def setUp(self):
        self.category = WebsiteCategory.objects.create(
            name='searching',
            description='Searching sites.',
            count=0,
        )

    def test_website_category_is_saved(self):
        category = WebsiteCategory.objects.get(name='searching')
        self.assertEqual(self.category, category)


class RoutingUrlsToViewsTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.views_names = {
            'list': 'WebsiteCategoryListView',
            'create': 'WebsiteCategoryCreateView',
        }
        self.urls = {
            'list': reverse('categories:list'),
            'create': reverse('categories:create'),
        }
        self.responses = {
            'list': self.client.get(self.urls['list']),
            'create': self.client.get(self.urls['create'])
        }

    def test_resolving_urls(self):
        for name, url in self.urls.items():
            func, args, kwargs = resolve(url)
            self.assertEqual(func.__name__, self.views_names[name])

    def test_responses(self):
        for name, response in self.responses.items():
            # TODO
            pass