from typing import Iterable
from django.db import models
from django.core.validators import MinLengthValidator
from django.utils.text import slugify

# Create your models here.

class Author(models.Model):

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return(f"{self.first_name} {self.last_name}")


class Tag(models.Model):
    caption = models.CharField(max_length=30)

    def __str__(self):
        return(f"{self.caption}")
    


class Post(models.Model):
    title = models.CharField(max_length=150)
    excerpt = models.CharField(max_length=200)
    image_name = models.ImageField(null=True,upload_to="data")
    date = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True,db_index=True,default=" ",null=True)
    content = models.TextField(validators=[MinLengthValidator(10)])
    author = models.ForeignKey(Author,on_delete=models.SET_NULL,null=True)
    tags = models.ManyToManyField(Tag)
    

    def __str__(self):
        return(f"{self.title}")
    
    def save(self,*args, **kwargs):
        self.slug = slugify(self.title)

        return super().save(*args, **kwargs)
    
class Comment(models.Model):
    user_name = models.CharField(max_length=50) 
    user_email = models.EmailField(max_length=100)
    user_comment = models.TextField(validators=[MinLengthValidator(2)])   
    post = models.ForeignKey(Post,on_delete=models.CASCADE,null=False)


