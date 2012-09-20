from django.db import models
from django.template.loader import render_to_string
from django.utils.translation import ugettext_lazy as _

from feincms.module.page.models import Page
from feincms.admin.item_editor import FeinCMSInline


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200, null=True, blank=True)
    ordering = models.PositiveIntegerField(default=0, null=True)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('ordering', 'name')
        verbose_name = _('category')
        verbose_name_plural = _('categories')


class Link(models.Model):
    name = models.CharField(max_length=100,
    description = models.CharField(max_length=200, blank=True)
    url = models.URLField()
    category = models.ForeignKey(Category)
    ordering = models.PositiveIntegerField(default=0, null=True)

    class Meta:
        ordering = ('ordering', 'name')
        verbose_name = _('link')
        verbose_name_plural = _('links')

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return self.url


class LinkContent(models.Model):
    """ Content type which renders all links from a selected category"""

    category = models.ForeignKey(Category, blank=True, null=True,
         help_text=_('Leave blank to list all categories.'))

    class Meta:
        abstract = True
        verbose_name = _('link list')
        verbose_name_plural = _('link lists')

    def render(self, **kwargs):
        if self.category:
            return render_to_string('content/links/category.html', {
                'category': self.category,
                }, context_instance=kwargs.get('context'))

        return render_to_string('content/links/all_categories.html', {
            'categories': Category.objects.all(),
            }, context_instance=kwargs.get('context'))


DEFAULT_CSS_CLASSES = (
    ('link', _('Link')),
    ('button', _('Button')),
)


class PrettyLinkContentInline(FeinCMSInline):
    raw_id_fields = ('page',)


class PrettyLinkContent(models.Model):
    """ Renders a link using a template """
    @classmethod
    def initialize_type(cls, LINK_CSS_CLASS_CHOICES=DEFAULT_CSS_CLASSES, **kwargs):
        cls.add_to_class('style',
            models.CharField(_('style'), max_length=20,
                choices=LINK_CSS_CLASS_CHOICES,
                default=LINK_CSS_CLASS_CHOICES[0][0],
                ))

    text = models.CharField(_('text'), max_length=200)
    url = models.URLField(_('URL'), blank=True)
    page = models.ForeignKey(Page, blank=True, null=True,
        verbose_name=_('page'),
        related_name='+',
        help_text=_('Optionally link directly to a page on this website.'))

    class Meta:
        abstract = True
        verbose_name = _('link')
        verbose_name_plural = _('links')

    def __unicode__(self):
        return self.text

    def render(self, **kwargs):
        if self.url:
            self.link = url
        elif self.page:
            self.link = self.page.get_absolute_url()
        else :
            self.link = "No URL defined."

        return render_to_string('content/links/single.html', {
            'content': self,
            }, context_instance=kwargs.get('context'))
