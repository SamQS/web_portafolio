from django.db import models
from django.db.models.fields import CharField
from django.db.models.fields.files import ImageField
import datetime

# Create your models here.
class Post(models.Model):
    title = CharField(max_length=100)
    description = CharField(max_length=250)
    image = ImageField(upload_to='blog/images/')
    date = models.DateField(datetime.date.today)