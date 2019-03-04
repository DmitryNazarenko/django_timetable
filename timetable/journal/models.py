from django.db import models
from django.utils.text import slugify

from django.contrib.auth.models import User

from time import time
# Create your models here.

def gen_slug(date):
    return slugify(date)+'-'+str(int((time()-int(time()))*135674))

class Record(models.Model):
    record = models.TextField(blank=True,db_index=True)
    date = models.DateField(blank=True)
    slug = models.SlugField(max_length = 50,blank=True,unique=True)
    user = models.ForeignKey(User,null=True,on_delete=models.SET_NULL)

    def __str__(self):
        return 'Date: '+str(self.date)

    def save(self,*args,**kwargs):
        if not self.id:
             self.slug = gen_slug(self.date)
        super().save(*args,**kwargs)
