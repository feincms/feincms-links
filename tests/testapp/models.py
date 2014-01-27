from django.utils.translation import ugettext_lazy as _

from feincms.module.page.models import Page
from feincms_links.models import LinkContent

Page.register_templates({
    'title': _('Standard template'),
    'path': 'base.html',
    'regions': (('main', _('Main content area')),)
})

PageLinkContent = Page.create_content_type(LinkContent)
