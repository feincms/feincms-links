from django.db import models
from django.utils.translation import ugettext_lazy as _


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
