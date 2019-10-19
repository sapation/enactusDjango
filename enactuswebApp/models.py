from django.contrib import admin
from django.conf import settings
from django.db import models
from django.db.models.signals import pre_save
from enactusApp.utils import unique_slug_generator
#from django.utils.text import slugify
#from django.urls import reverse

# Create your models here.
def upload_location(instance, filename):
    return "%s/%s" %(instance.id, filename)

class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    title = models.CharField(max_length= 120)
    slug = models.SlugField(max_length=250, null=True, blank=True)
    image = models.ImageField(upload_to=upload_location ,null=True, blank=True,
              width_field="width_field",
              height_field="height_field")
    height_field = models.IntegerField(default = 0)
    width_field = models.IntegerField(default = 0)
    content = models.TextField()
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=True)
    draft = models.BooleanField(default=False)
    published = models.DateField(auto_now=True, auto_now_add=False)


    def __str__(self):
        return self.title
        
    def get_absolute_url(self):
        return "posts/%s" %(self.slug)   
    #     reverse('blog-details', kwargs={'slug_text': 'slug'})
         

def slug_generator(sender, instance, *args, **kwargs):
    if not instance.slug:
         instance.slug= unique_slug_generator(instance)

pre_save.connect(slug_generator, sender=Post)
    


class ImageUpload(models.Model):
    title = models.CharField(max_length= 120)
    image = models.ImageField(upload_to=upload_location ,null=True, blank=True,
              width_field="width_field",
              height_field="height_field")
    height_field = models.IntegerField(default = 0)
    width_field = models.IntegerField(default = 0)  
    timestamp = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title                  
