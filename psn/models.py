from datetime import datetime

from django.db import models
from django.contrib.auth.models import User
from psn.util import *
    
class SocialNetworkProfile(models.Model):
    user = models.ForeignKey(User, primary_key=False, db_index=True, related_name=_('social_network_profiles'), raw_id_admin=True)
    network_id = models.CharField(maxlength=16, choices=NETWORK_IDS, db_index=True)
    username = models.CharField(maxlength=64)
    date_added = models.DateTimeField(_('date added'), auto_now_add=True)
    date_verified = models.DateTimeField(_('date verified'), default=datetime.now)
    is_verified = models.BooleanField(default=False)
    
    def __str__(self):
        return self.network_id
        
    # get the display name for a social network
    def _get_network_name(self):
        for k,v in NETWORK_IDS:
            if k == self.network_id:
                return v
        else:
            return None
    network_name = property(_get_network_name)

    # get the url for a social network with the username/id inserted
    def _get_profile_url(self):
        try:
            return NETWORK_URLS[self.network_id] % str(self.username)
        except:
            return None
    profile_url = property(_get_profile_url)
    
    class Admin:
        pass

class InstantMessengerProfile(models.Model):
    user = models.ForeignKey(User, primary_key=False, db_index=True, related_name=_('instant_messenger_profiles'), raw_id_admin=True)
    messenger_id = models.CharField(maxlength=16, choices=MESSENGER_IDS, db_index=True)
    username = models.CharField(maxlength=64)
    date_added = models.DateTimeField(_('date added'), auto_now_add=True)
    date_verified = models.DateTimeField(_('date verified'), default=datetime.now)
    is_verified = models.BooleanField(default=False)
    
    def __str__(self):
        return self.username
    
    # get the long name for an IM service
    def _get_full_messenger_name(self):
        for k,v in MESSENGER_IDS:
            if k == self.messenger_id:
                return v
        else:
            return None
    full_messenger_name = property(_get_full_messenger_name)
    
    # get the display name for an IM service
    def _get_messenger_name(self):
        try:
            return MESSENGER_NAMES[self.messenger_id]
        except:
            return None
    messenger_name = property(_get_messenger_name)

    # get the url to start a chat with the username/id provided
    def _get_messenger_url(self):
        try:
            return MESSENGER_URLS[self.messenger_id] % str(self.username)
        except:
            return None
    messenger_url = property(_get_messenger_url)

    class Admin:
        pass
        
class WebsiteProfile(models.Model):
    user = models.ForeignKey(User, primary_key=False, db_index=True, related_name=_('website_profiles'), raw_id_admin=True)        
    name = models.CharField(maxlength=64)
    url = models.URLField(verify_exists=True)
    date_added = models.DateTimeField(_('date added'), auto_now_add=True)
    date_verified = models.DateTimeField(_('date verified'), default=datetime.now)
    is_verified = models.BooleanField(default=False)
    
    def __str__(self):
        return self.url
    
    class Admin:
        pass