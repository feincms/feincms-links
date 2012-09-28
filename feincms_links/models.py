from django.db import models
from django.template.loader import render_to_string
from django.utils.translation import ugettext_lazy as _

from feincms.module.page.models import Page
from feincms.admin.item_editor import FeinCMSInline


class Category(models.Model):
    name = models.CharField(_('name'), max_length=100)
    description = models.CharField(_('description'), max_length=200,
        blank=True)
    ordering = models.PositiveIntegerField(_('ordering'), default=0)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('ordering', 'name')
        verbose_name = _('category')
        verbose_name_plural = _('categories')


class Link(models.Model):
    name = models.CharField(_('name'), max_length=100)
    description = models.CharField(_('description'), max_length=200,
        blank=True)
    url = models.URLField(_('URL'))
    category = models.ForeignKey(Category, verbose_name=_('category'))
    ordering = models.PositiveIntegerField(_('ordering'), default=0)

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
        verbose_name=_('category'),
         help_text=_('Leave blank to list all categories.'))

    class Meta:
        abstract = True
        verbose_name = _('link list')
        verbose_name_plural = _('link lists')

    def render(self, **kwargs):
        ctx = {'content': self}
        if self.category:
            ctx['links'] = self.category.link_set.all()
        else:
            ctx['links'] = Link.objects.order_by(
                'category__ordering',
                'category__name',
                'ordering',
                'name',
                )

        return render_to_string('content/links/default.html', ctx,
            context_instance=kwargs.get('context'))
