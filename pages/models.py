from django.db import models
from django.core.exceptions import ValidationError
from django.db.models.signals import pre_save
# Create your models here.

LAYOUT_CHOICES = (
    ('standard', 'Standard'),
    ('stacked', 'Stacked'),
)

from .utils import unique_slug_generator


def layout_validator(value):
    if value[0] != "#":
        raise ValidationError("Must start with #")
    if len(value) == 4 or len(value) == 7:
         return value
    raise ValidationError("Incorrect length")

class Page(models.Model):
    title               = models.CharField(max_length=220)
    title_description   = models.TextField(blank=True, null=True)
    title_btn           = models.CharField(max_length=50, default='Join')
    title_btn_url       = models.CharField(max_length=50, blank=True, null=True)
    jumbotron_text_color = models.CharField(max_length=7, default='#000000', validators=[layout_validator])
    jumbotron_bg_color   = models.CharField(max_length=7, default='#eeeeee', validators=[layout_validator])
    content             = models.TextField(blank=True, null=True)
    show_nav            = models.BooleanField(default=True, help_text='Show Navigation Bar?')
    nav_color           = models.CharField(max_length=7, default='#000000', validators=[layout_validator])
    layout              = models.CharField(max_length=20, choices=LAYOUT_CHOICES, default='standard')
    video_embed         = models.TextField(null=True, blank=True)
    slug                = models.SlugField(default='page-slug', blank=True)
    featured            = models.BooleanField(default=False)
    active              = models.BooleanField(default=True)
    leave_capture       = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if self.featured:
            qs = Page.objects.filter(featured=True).exclude(pk=self.pk)
            if qs.exists():
                qs.update(featured=False)
        super(Page, self).save(*args, **kwargs)


    def __str__(self):
        return self.title

def pre_save_receiver_page_model(sender, instance, *args, **kwargs):
    if instance.slug == 'page-slug' or instance.slug == '':
        instance.slug = unique_slug_generator(instance)

pre_save.connect(pre_save_receiver_page_model, sender=Page)





