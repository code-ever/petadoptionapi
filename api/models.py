from typing import Iterable
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.core.mail import send_mail,EmailMultiAlternatives
from django.template.loader import render_to_string

# Create your models here.

class User(AbstractUser):
    username = models.CharField(max_length=200,null=True, blank=True)
    email = models.EmailField(unique=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    def __str__(self):
      return self.email
  
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.DO_NOTHING, null=True, blank=True)
    first_name = models.CharField(max_length=200, blank=True, null=True)
    last_name = models.CharField(max_length=200, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField(upload_to='profiles', null=True, blank=True)
    verified = models.BooleanField(default=False)
    
    def __str__(self):
        return str(self.first_name) if self.first_name else "Unnamed Pet"
    
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
    
post_save.connect(create_user_profile, sender=User)
post_save.connect(save_user_profile, sender=User)
    
class Category(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    
    def __str__(self):
        return self.name
    
class Subcategory(models.Model):
    def category_upload(instance, filename):
        return f"sub_categories/{instance.name}/{filename}"
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='categoryname')
    name = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField(upload_to=category_upload,blank=True, null=True)
    
    def __str__(self):
        return f'{self.category}::{self.name}'   

class Uploadpets(models.Model):
    def Image_upload(instance, filename):
      return f"categories/{instance.petname}/{filename}"
    POST_CHOICE = [
      ('family','family'),
      ('apatmentdog','apatmentdog')
    ]
    subcategory = models.ForeignKey(Subcategory,on_delete=models.CASCADE,blank=True, null=True)
    # category = models.ForeignKey(Category,on_delete=models.CASCADE,blank=True, null=True)
    family =  models.CharField(max_length=200, blank=True, null=True)
    petname = models.CharField(max_length=200, blank=True, null=True)
    breed = models.CharField(max_length=300, blank=True, null=True)
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=200,blank=True, null=True)
    description = models.CharField(max_length=300, blank=True, null=True)
    sex = models.CharField(max_length=20,null=True,blank=True)
    adoption_fee = models.CharField(max_length=200, null=True,blank=True)
    species = models.CharField(max_length=300,null=True,blank=True)
    sRescueID = models.CharField(max_length=300,null=True,blank=True)
    currentSize = models.CharField(max_length=300, blank=True, null=True)
    fenceRequired = models.CharField(max_length=300, blank=True, null=True)
    housetrained = models.CharField(max_length=300, blank=True, null=True)
    obedienceTraining = models.CharField(max_length=300, blank=True, null=True)
    exerciseNeeds = models.CharField(max_length=300, blank=True, null=True)
    ownerExperience = models.CharField(max_length=300, blank=True, null=True)
    reaction_to_New_People = models.CharField(max_length=300, blank=True, null=True)
    images = models.ImageField(upload_to=Image_upload, null=True, blank=True)
    postleble = models.CharField(max_length=200,choices=POST_CHOICE,blank=True, null=True)
    slug = models.SlugField(max_length=255,default=None,null=True,blank=True)
    uploade_date = models.DateField(auto_now_add=True,blank=True,null=True)
    published = models.DateField(auto_now=True,blank=True,null=True)
    
    
    def __str__(self):
        return str(self.petname) if self.petname else "Unnamed petname"
    
    def get_absolute_url(self):
        return f'/{self.slug}/'
   
    
class Contact(models.Model):
    name = models.CharField(max_length=200, blank=False,null=False)
    email = models.EmailField(max_length=200, blank=False,null=False)
    phone = models.CharField(max_length=200, blank=False,null=False)
    location = models.CharField(max_length=200, blank=False,null=False)
    howsoon = models.CharField(max_length=200, blank=False,null=False)
    message = models.TextField(max_length=200, blank=False,null=False)

    def __str__(self):
        return self.name
    
class Enquiry(models.Model):
    firstName = models.CharField(max_length=200,null=True,blank=True)
    lastName = models.CharField(max_length=200,null=True,blank=True)
    address = models.CharField(max_length=200,null=True,blank=True)
    mobile = models.CharField(max_length=200,null=True,blank=True)
    subject = models.CharField(max_length=200,null=True,blank=True)
    location = models.CharField(max_length=200,null=True,blank=True)
    categoryRequest = models.CharField(max_length=200,null=True,blank=True)
    petIntres = models.CharField(max_length=200,null=True,blank=True)
    messagedata = models.TextField(null=True,blank=True)
    
    def __str__(self):
        return self.petIntres
        