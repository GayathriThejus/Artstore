from django.db import models

# Create your models here.
class paintings(models.Model):
   
    art=models.ImageField(upload_to='paintings', height_field=None, width_field=None, max_length=100)