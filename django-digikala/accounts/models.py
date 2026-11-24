from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin

# Create your models here.

class CustomUserManager(BaseUserManager):
    # overwrite _create_user which is defined in the parent by email 
    def _create_user(self,phone,password=None,**extra_fields):
        first_name = extra_fields.get('first_name')
        last_name = extra_fields.get('last_name')
        if not first_name or not last_name:
            raise ValueError('The names field must be set')
        if not phone:
            raise ValueError('The phone field must be set')
        # create an instance from user 
        user = self.model(phone=phone, **extra_fields)
        # use setpassword to save a hash pasword no the password itself directly 
        user.set_password(password)
        # for saving in the database we should use save
        user.save(using=self._db)
        return user
    
    def create_user(self, phone,password=None,**extra_fields):
                # setdefault 
        # means if there is no is_staff and is_active keyword add these ones otherwise the values would be as it is in the extra_fields
        extra_fields.setdefault('is_staff',False)
        extra_fields.setdefault('is_active',True)
        return self._create_user(phone, password, **extra_fields)
    
    def create_superuser(self, phone, password=None,**extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_active',True)
        extra_fields.setdefault('is_superuser',True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True')
        
        if extra_fields.get('is_active') is not True:
            raise ValueError('Superuser must have is_active=True')
        
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True')
        
        return self.create_user(phone,password, **extra_fields)


class User(AbstractBaseUser,PermissionsMixin):
    phone = models.CharField(max_length=11, unique=True, verbose_name='phone')
    first_name = models.CharField(max_length=30, default='')
    last_name = models.CharField(max_length=30, default='')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
# objects یک instance از CustomUserManager است.
    objects= CustomUserManager()
    # یلد شناسایی کاربر phone هست
    USERNAME_FIELD = 'phone'
    # what forms input should be includ in creating a user 
    REQUIRED_FIELDS = ['first_name','last_name']
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    

class CustomerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )
    
class  SellerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    