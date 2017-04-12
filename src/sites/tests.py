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
        self.website = Website.objects.create(
            url='www.google.com',
            title='Google',
            meta_description='Google searching.',
            alexa_rank=1,
            category=self.category,
        )
        self.page = WebPage.objects.create(
            title='google',
            website=self.website,
            url='https://www.google.com/doodles',
            meta_description='Google doodles',
        )

    def test_web_page_properly_saved(self):
        page = WebPage.objects.get(title='google')
        self.assertEqual(page, self.page)

    def test_website_is_saved(self):
        google = Website.objects.get(url='www.google.com')
        self.assertEqual(
            google.title,
            'Google',
            'google\'s title does not equals \'Google\''
        )
        self.assertEqual(google.category.name, 'searching')


class RoutingUrlsToViewsTestCase(TestCase):

    def setUp(self):
        self.category = WebsiteCategory.objects.create(
            name='searching',
            description='Searching sites.',
            count=0,
        )
        self.website = Website.objects.create(
            url='www.google.com',
            title='Google',
            meta_description='Google searching.',
            alexa_rank=1,
            category=self.category,
        )
        self.client = Client()
        self.views_names = {
            'list': 'WebsiteListView',
            'create': 'WebsiteCreateView',
            'detail': 'WebsiteDetailView',
        }
        self.urls = {
            'list': reverse('sites:list'),
            'create': reverse('sites:create'),
            'detail': reverse('sites:detail', kwargs={'pk': 1}),
        }
        self.responses = {
            'list': self.client.get(self.urls['list']),
            'create': self.client.get(self.urls['create']),
            'detail': self.client.get(self.urls['detail']),
        }

    def test_resolving_urls(self):
        for name, url in self.urls.items():
            func, args, kwargs = resolve(url)
            self.assertEqual(func.__name__, self.views_names[name])
            if kwargs:
                self.assertEqual(kwargs['pk'], '1')

    def test_responses(self):
        for name, response in self.responses.items():
            self.assertEqual(response.status_code, 200, name)