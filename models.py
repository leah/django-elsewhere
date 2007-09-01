from django.db import models
from django.contrib.auth.models import User
from django_psn.util import NETWORK_IDS, MESSENGER_IDS
    
class SocialNetworkProfile(models.Model):
    user = models.ForeignKey(User, primary_key=False, db_index=True, related_name=_('social_network_profiles'), raw_id_admin=True)
    network_id = models.CharField(maxlength=16, choices=NETWORK_IDS, db_index=True)
    username = models.CharField(maxlength=64)
    date_added = models.DateTimeField(_('date added'), default=models.LazyDate(), auto_now_add="true")
    date_verified = models.DateTimeField(_('date verified'), default=models.LazyDate())
    is_verified = models.BooleanField(default=False)
    
    def __str__(self):
        return self.network_id
    
    class Admin:
        pass

class InstantMessengerProfile(models.Model):
    user = models.ForeignKey(User, primary_key=False, db_index=True, related_name=_('instant_messenger_profiles'), raw_id_admin=True)
    messenger_id = models.CharField(maxlength=16, choices=MESSENGER_IDS, db_index=True)
    username = models.CharField(maxlength=64)
    date_added = models.DateTimeField(_('date added'), default=models.LazyDate(), auto_now_add="true")
    date_verified = models.DateTimeField(_('date verified'), default=models.LazyDate())
    is_verified = models.BooleanField(default=False)
    
    def __str__(self):
        return self.username
    
    class Admin:
        pass
        
class WebsiteProfile(models.Model):
    user = models.ForeignKey(User, primary_key=False, db_index=True, related_name=_('website_profiles'), raw_id_admin=True)        
    name = models.CharField(maxlength=64)
    url = models.CharField(maxlength=250)
    date_added = models.DateTimeField(_('date added'), default=models.LazyDate(), auto_now_add="true")
    date_verified = models.DateTimeField(_('date verified'), default=models.LazyDate())
    is_verified = models.BooleanField(default=False)
    
    def __str__(self):
        return self.url
    
    class Admin:
        pass