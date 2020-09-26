from django.db import models
from datetime import datetime, timedelta
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from gst_field.modelfields import GSTField, PANField
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError('User must have an email address')
        if not username:
            raise ValueError('User must have an username')

        user = self.model(
            email = self.normalize_email(email),
            username = username
        )
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser(self, email, username, password=None):
        user = self.create_user(
            email = self.normalize_email(email),
            password = password,
            username = username
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self.db)
        return user

class OwnerManager(BaseUserManager):
 
    def create_owner(self, username, email, company_name, GST, PAN, password=None):
        if email is None:
            raise TypeError('Users must have an email address.')
        owner = Owner(username = username,
                    company_name= company_name,
                    GST = GST,
                    PAN = PAN, 
                    email=self.normalize_email(email),
                )
        owner.is_staff = True
        owner.has_perm('organizations.view_organizations')
        owner.set_password(password)
        owner.save()
        return owner 
 
class ExecutiveManager(BaseUserManager):
 
    def create_executive(self, username, email, designation, department, password=None):
        if email is None:
            raise TypeError('Users must have an email address.')
        executive = Executive(username = username, 
                          email=self.normalize_email(email),
                          designation = designation, 
                          department = department)
        executive.is_staff = True
        executive.set_password(password)
        executive.save()
        return executive
 
 
class EmployeeManager(BaseUserManager):
 
    def create_employee(self, username, email, role, department, password=None):
        if email is None:
            raise TypeError('Users must have an email address.')
        employee = Employee(username = username, 
                            email=self.normalize_email(email),
                            role=role, department=department)
        employee.set_password(password)
        employee.save()
        return employee


class User(AbstractBaseUser, PermissionsMixin):

    USER_TYPES = (
       ("Owner", "Owner"),
       ("Executive", "Executive"),
       ("Employee", "Employee")
    )

    email = models.EmailField(unique=True)
    username = models.CharField(max_length=30, unique=True)
    user_type = models.CharField(max_length=50, choices=USER_TYPES, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
 
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    objects = UserManager()

 
    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

    def __str__(self):
        return self.email

class Owner(User, PermissionsMixin):
    company_name = models.CharField(max_length=50)
    GST = GSTField()
    PAN = PANField()


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'company_name', 'GST', 'PAN']
 
    objects = OwnerManager()
 
    def __str__(self):
        return self.username

class Executive(User, PermissionsMixin):
    designation = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
 
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'designation', 'department']
 
    objects = ExecutiveManager()
 
    def __str__(self):
        return self.username
 
class Employee(User, PermissionsMixin):
    role = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
 
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'role', 'department']
 
    objects = EmployeeManager()
 
    def __str__(self):
        return self.username

@receiver(post_save, sender = User)
def user_create_auth_token(sender, instance = None, created = False, **kwargs):
    if created:
        Token.objects.create(user = instance)


@receiver(post_save, sender = Owner)
def owner_create_auth_token(sender, instance = None, created = False, **kwargs):
    if created:
        Token.objects.create(user = instance)

@receiver(post_save, sender = Executive)
def executive_create_auth_token(sender, instance = None, created = False, **kwargs):
    if created:
        Token.objects.create(user = instance)

@receiver(post_save, sender = Employee)
def employee_create_auth_token(sender, instance = None, created = False, **kwargs):
    if created:
        Token.objects.create(user = instance)