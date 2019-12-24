from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel


class HomePage(Page):
    head = RichTextField(blank=True)
    body = RichTextField(blank=True)
    banner_image = models.ForeignKey(
        'wagtailimages.Image', null=True, blank=True,
        on_delete=models.SET_NULL, related_name='+'
    )
    content_panels = Page.content_panels + [
        FieldPanel('head', classname="full"),
        FieldPanel('body', classname="full"),
        ImageChooserPanel('banner_image'),
    ]
    def get_context(self, request, *args, **kwargs):
        context = super(HomePage, self).get_context(request, *args, **kwargs)
        context['menuitems'] = self.get_children().filter(
            live=True, show_in_menus=True)

        return context

class HomeIndexPage(Page):
    text = RichTextField(blank=True)
    postedby = RichTextField(blank=True)
    image = models.ForeignKey(
        'wagtailimages.Image', null=True, blank=True,
        on_delete=models.SET_NULL, related_name='+'
    )
    content_panels = Page.content_panels + [
        FieldPanel('text', classname="full"),
        FieldPanel('postedby', classname="full"),
        ImageChooserPanel('image'),
    ]

  


    