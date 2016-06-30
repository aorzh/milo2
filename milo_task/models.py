from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.core.validators import MinValueValidator, MaxValueValidator
import random


class CustomUserManager(BaseUserManager):
    def create_user(self, username,  password=None):
        user = self.model(
            username=username
        )
        user.random_number = random.randint(0, 100)  # returns a random integer
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password):
        user = self.create_user(username=username, password=password,)
        user.is_admin = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser):
    username = models.CharField(
        max_length=1000,
        verbose_name=u'Username',
        unique=True,
    )
    birthday = models.DateField(null=True)
    random_number = models.PositiveIntegerField(default=random.randint(1, 100),
                                                validators=[MinValueValidator(1), MaxValueValidator(100)])

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    objects = CustomUserManager()
    USERNAME_FIELD = 'username'

    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return self.username

    def __unicode__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        # Handle whether the user has a specific permission?"
        return True

    def has_module_perms(self, app_label):
        # Handle whether the user has permissions to view the app `app_label`?"
        return True

    @property
    def is_staff(self):
        # Handle whether the user is a member of staff?"
        return self.is_admin

    def meta(self):
        return self._meta

    class Meta:
        verbose_name = u"User"
        verbose_name_plural = u"Users"