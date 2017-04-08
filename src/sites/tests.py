from django.test import TestCase
from .models import WebPage, Website, WebsiteCategory


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