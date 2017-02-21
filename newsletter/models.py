from django.db import models

# Create your models here.

class Join(models.Model):
    email = models.EmailField() # unqiue=True
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self): # __unicode__
        return self.email