from django.db import models
from datetime import datetime
from account.models import User
# Create your models here.


class Listing(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    photo_main = models.URLField(blank=True)
    # work photos
    photo_1 = models.URLField(blank=True)
    photo_2 = models.URLField(blank=True)
    photo_3 = models.URLField(blank=True)
    photo_4 = models.URLField(blank=True)
    photo_5 = models.URLField(blank=True)
    photo_6 = models.URLField(blank=True)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.title
    
class Cart(models.Model):
    user = models.ForeignKey(User,models.CASCADE,null=True,blank=True)
    product = models.ForeignKey(Listing,models.CASCADE,null=True,blank=True)
    