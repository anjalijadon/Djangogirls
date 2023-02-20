from django.db import models
from django.utils import timezone
#from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now
from django_extensions.db.fields import AutoSlugField
from django.utils.safestring import mark_safe
from django_ckeditor_5.fields import CKEditor5Field

class User(AbstractUser):
    email = models.EmailField(max_length=255,blank=True,null=True)
    gender = models.CharField(max_length=20)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    mobile_no = models.CharField(max_length=15)
    image = models.ImageField(upload_to ='image/')

    
    def __str__(self):
        return self.email

class Category(models.Model):
    
    name = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from=('name'), unique=True, max_length=255)
    
    
    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name

class Tag(models.Model):
    
    name=models.CharField(max_length=200)
    slug = AutoSlugField(populate_from=('name'), unique=True, max_length=255)
    

    def __str__(self):
        return self.name

class Post(models.Model):
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    slug = AutoSlugField(populate_from=('title'), unique=True, max_length=255)
    text = CKEditor5Field('Text', config_name='extends')
    featured_image = models.ImageField(upload_to="featured_images/")
    thumbnail_image = models.ImageField(upload_to="thumbnail_images/")
    created_date=models.DateTimeField(default=timezone.now)
    published_date=models.DateTimeField(blank=True,null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag)
    
    def thumbnail(self): 
        return mark_safe(f'<img src = "{self.thumbnail_image.url}" width = "150"/>')
         
    def featured(self): 
        return mark_safe(f'<img src = "{self.featured_image.url}" width = "150"/>')
         
    def publish(self):
        self.published_date=timezone.now()
        self.save()
    
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    name = models.CharField(max_length=50)
    slug = AutoSlugField(populate_from=('name'), unique=True)
    email = models.EmailField(max_length=100, default='abc@gmail.com')
    comment = models.TextField(max_length = 1000, default = 'Good')
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=now)

    class Meta:
        ordering = ('-timestamp',)

    def __str__(self):
        return self.name

