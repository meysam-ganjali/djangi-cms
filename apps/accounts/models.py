from django.db import models
from django_jalali.db import models as jmodels
import jdatetime
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.base_user import BaseUserManager
from django.utils.html import mark_safe


class CustomerUserManager(BaseUserManager):
    def create_user(self, user_phone, password, name='', family='', image=None, active_code=None):
        if not user_phone:
            raise ValueError('شماره موبایل را وارد نکرده اید')
        user = self.model(user_phone=user_phone, name=name, family=family, image=image, active_code=active_code)
        if len(password) < 6:
            raise ValueError('طول کلمه عبور باید بیشتر از 6 باشد')
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, user_phone, name, family, password):
        user = self.create_user(user_phone, password, name, family)
        user.is_active = True
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    user_phone = models.CharField(max_length=15, unique=True, verbose_name='شماره موبایل')
    image = models.ImageField(upload_to='users/avatar/', null=True, blank=True)
    name = models.CharField(max_length=1000, verbose_name='نام')
    active_code = models.CharField(max_length=10, verbose_name='کد فعالسازی', null=True, blank=True)
    family = models.CharField(max_length=50, verbose_name='نام خانوادگی', null=True, blank=True)
    register_date = jmodels.jDateField(default=jdatetime.date.today(), verbose_name='تاریخ ثبت نام')
    is_active = models.BooleanField(default=False, verbose_name='کاربر فعال باشد یا نه؟')
    is_admin = models.BooleanField(default=False, verbose_name='کاربر مدیر باشد یا نه؟')

    USERNAME_FIELD = 'user_phone'
    REQUIRED_FIELDS = ['name', 'family']
    objects = CustomerUserManager()

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'

    def __str__(self):
        return f'{self.name} {self.family}'

    def get_user_img(self):
       if self.image:
           return mark_safe('<img src="/media/%s" width="50" height="50" style="border-radius:5px;" />' % self.image)
       return mark_safe(
            '<img src="/media/no-image.png" width="50" height="50" style="border-radius:5px;" />')

    get_user_img.short_description = ''
    get_user_img.allow_tags = True

    @property
    def is_staff(self):
        return self.is_admin
