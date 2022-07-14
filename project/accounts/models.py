from django.db import models
from django.contrib.auth.models import  AbstractBaseUser 
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.base_user import BaseUserManager
from django.utils import timezone
from django.urls import reverse

class CustomUserManager(BaseUserManager):
    def create_user(self, username, password, **extra_fields):
        if not username:
            raise ValueError(_('The Username must be set'))
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(username, password, **extra_fields) 



class Permission(models.Model):
    title = models.CharField(_("title"), max_length=100)

    def __str__(self) :
        return self.title






class User(AbstractBaseUser):
    username = models.CharField(_('username'), max_length=100,unique=True,null=True,blank=True)
    permission = models.ManyToManyField( Permission , verbose_name=_("per mission"), blank=True , through='User_Permission') 
    is_superuser = models.BooleanField(
        _('superuser status'),
        default=False,
        help_text=_(
            'Designates that this user has all permissions without '
            'explicitly assigning them.'
        ),
    )
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)


    objects = CustomUserManager()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser

    def get_absolute_url(self):
        return reverse("profile_staff", kwargs={"pk": self.pk})
    
    


class User_Permission(models.Model):
    user = models.ForeignKey(User, verbose_name=_("user"), on_delete=models.CASCADE)
    per_user = models.ForeignKey(Permission, verbose_name=_("permission"), on_delete=models.CASCADE)
    is_confermid = models.BooleanField(_("is_confermid") , default=True)





class Customer(models.Model ):
    id_number = models.BigAutoField(primary_key=True,blank=True , unique=True)
    username = models.CharField(_("username"), max_length=60)
    phone_number = models.CharField(_("phone number"),max_length=11)




    def save(self, *args, **kwargs):
       if not Customer.objects.count():
          self.id_number = 1000
       else:
          self.id = Customer.objects.last().id_number + 1
       super(Customer, self).save(*args, **kwargs)

    def __str__(self):
        return self.username
    







        


    




