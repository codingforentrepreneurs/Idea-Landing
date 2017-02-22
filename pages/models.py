from django.db import models

# Create your models here.

class Page(models.Model):
    title               = models.CharField(max_length=220)
    title_description   = models.TextField(blank=True, null=True)
    title_btn           = models.CharField(max_length=50, default='Join')
    title_btn_url       = models.CharField(max_length=50, blank=True, null=True)
    content             = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title