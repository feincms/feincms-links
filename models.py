from django.db import models
from django.utils.translation import ugettext as _

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200, null=True, blank=True)
    ordering = models.PositiveIntegerField(default=0, null=True)
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        ordering = ('ordering','name')
        get_latest_by = 'id'
        verbose_name_plural = _('Categories')
    
class Link(models.Model):
    name = models.CharField(max_length=100, \
        help_text=_('displayed name for the link'))
    description = models.CharField(max_length=200, null=True, blank=True, \
        help_text=_('used for title attribut. is displayed on rollover.'))
    url = models.URLField(verify_exists=False)
    category = models.ForeignKey(Category)
    ordering = models.PositiveIntegerField(default=0, null=True)
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        ordering = ('ordering','name', )
        get_latest_by = 'id'