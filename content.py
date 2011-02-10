from django.db import models
from django.template.loader import render_to_string
from django.utils.translation import ugettext_lazy as _

from models import Category
from django.template.context import RequestContext

class LinkContent(models.Model):
    
    category = models.ForeignKey(Category, blank=True, null=True,
                                 help_text=_('Leave blank to list all categories.'))
    
    class Meta:
        abstract = True
        verbose_name = _('Linklist')
        verbose_name_plural = _('Linklists')
    
    def render(self, **kwargs):
        request = kwargs.get('request')

        if self.category:
            return render_to_string('content/links/category.html', 
                                    {'category': self.category}, context_instance=RequestContext(request))

        categories = Category.objects.all()
        return render_to_string('content/links/all_categories.html', {
                'categories' : categories}, context_instance=RequestContext(request))
