from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models

# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, email, password=None,first_name=None,last_name=None, is_active=True, is_staff=False, is_admin=False, is_student=False):
        if not email:
            raise ValueError("Must have Email")
        if not password:
            raise ValueError("Must have Password")

        user_obj = self.model(
            email=self.normalize_email(email)
        )
        user_obj.set_password(password)
        user_obj.first_name = first_name
        user_obj.last_name = last_name
        user_obj.staff = is_staff
        user_obj.admin = is_admin
        user_obj.active = is_active
        user_obj.save(using=self._db)

        return user_obj

    def create_staffuser(self, email, password=None):
        user = self.create_user(
            email,
            password=password,
            is_staff=True,
            is_active=True,
        )
        return user

    def create_student(self, email, password=None):
        user = self.create_user(
            email,
            password=password,
            is_student=True,
            is_staff=False,
            is_active=False,
        )
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(
            email,
            password=password,
            is_staff=True,
            is_admin=True,
            is_active=True,
        )
        return user


class User(AbstractBaseUser):
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    active = models.BooleanField(default=True)  # able to login
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    student = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'  # username
    REQUIRED_FIELDS = []  # what fields are ask when running python manage.py createsuperuser

    objects = UserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_active(self):
        return self.active

    @property
    def is_student(self):
        return self.student
