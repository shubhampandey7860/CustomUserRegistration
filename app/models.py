from django.db import models

# Create your models here
from django.contrib.auth.models import AbstractUser,BaseUserManager,PermissionsMixin

class UserProfileManager(BaseUserManager):
    
    def create_user(self,email,first_name,last_name,password=None):
        if not email:
            raise ValueError('email is not provided')
        nemail =self.normalize_email(email)
        uo = self.model(email=nemail,first_name=first_name,last_name=last_name)
        uo.set_password(password)
        uo.save()
        return uo 
    def create_superuser(self,email,first_name,last_name,password):
        uo = self.create_user(email,first_name,last_name,password)
        uo.is_staff = True
        uo.is_super_user = True
        uo.save()
        
        

class UserProfile(AbstractUser,PermissionsMixin):
    email = models.EmailField(max_length=100,primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    is_active=models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    
    objects = UserProfileManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name','last_name']
    
    
    
    
