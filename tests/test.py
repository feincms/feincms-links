from django.test import TestCase
from django.test.client import Client

from feincms.module.page.models import Page
from feincms_links.models import Category, Link
from tests.models import PageLinkContent


class LinkContentTest(TestCase):

    def setUp(self):
        category = Category.objects.create(
            name='Test'
        )
        self.link = Link.objects.create(
            name='TestLink',
            url='http://test.com',
            category=category,
        )
        page = Page.objects.create(
            title='TestPage',
            slug='testpage',

        )
        self.content = PageLinkContent.objects.create(
            parent=page,
            region='main',
            category=category
        )

    def test_link_absolute_url(self):
        url = self.link.get_absolute_url()
        self.assertEqual(url, 'http://test.com')

    def test_link_content_render(self):
        html = self.content.render(kwargs={'context': {}})
        self.assertIn('TestLink', html)
        self.assertIn('http://test.com', html)

    def test_feincms_integration(self):
        res = Client().get('/testpage/')
        self.assertContains(res, 'TestLink')
        self.assertContains(res, 'http://test.com')

