from django.db import models
from django import forms
from django.template.loader import render_to_string
from django.utils.translation import ugettext_lazy as _

from models import Category
from django.template.context import RequestContext
from feincms.module.page.models import Page
from django.contrib.admin.widgets import ForeignKeyRawIdWidget
from feincms.admin.editor import ItemEditorForm

class LinkContent(models.Model):
    """ Content type which renders all links from a selected Category """
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
                                    {'category': self.category}, 
                                    context_instance=RequestContext(request))

        categories = Category.objects.all()
        return render_to_string('content/links/all_categories.html', {
                'categories' : categories}, context_instance=RequestContext(request))
        
DEFAULT_CSS_CLASSES = (('link', _('Link')),
                       ('button', _('Button')),
)

class PrettyLinkContent(models.Model):
    """ Renders a link using a template """
    @classmethod
    def initialize_type(cls, LINK_CSS_CLASS_CHOICES=DEFAULT_CSS_CLASSES, **kwargs):
        cls.add_to_class('style', models.CharField(max_length=20, choices=LINK_CSS_CLASS_CHOICES,
                                  default=LINK_CSS_CLASS_CHOICES[0][0]))
        class PrettyLinkContentAdminForm(ItemEditorForm):
            page = forms.ModelChoiceField(queryset=Page.objects.active(),
                widget=ForeignKeyRawIdWidget(PrettyLinkContent._meta.get_field('page').rel),
                label=_('Page'))
        cls.feincms_item_editor_form = PrettyLinkContentAdminForm

    text = models.CharField(_('Text'), max_length=200)
    url = models.URLField(_('URL'), blank=True)
    page = models.ForeignKey(Page, blank=True, null=True, verbose_name=_('Page'),
                             related_name="%(app_label)s_%(class)s_related",
                             help_text = _('Optionally link directly to a page on this website'))
    
    class Meta:
        abstract = True
        verbose_name = _('Link')
        verbose_name_plural = _('Links')
    
    def __unicode__(self):
        return unicode(self.text)
    
    def render(self, **kwargs):
        request = kwargs.get('request')
        if self.url:
            self.link = url
        elif self.page:
            self.link = self.page.get_absolute_url()
        else :
            self.link = "No URL defined."
        return render_to_string('content/links/single.html', {'content': self }, 
                                RequestContext(request))