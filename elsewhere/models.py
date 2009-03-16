from datetime import datetime

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.contrib import admin

from elsewhere.util import *
    
class SocialNetworkProfile(models.Model):
    user = models.ForeignKey(User, db_index=True, related_name='social_network_profiles')
    network_id = models.CharField(max_length=16, choices=NETWORK_IDS, db_index=True)
    username = models.CharField(max_length=64)
    date_added = models.DateTimeField(_('date added'), auto_now_add=True)
    date_verified = models.DateTimeField(_('date verified'), default=datetime.now)
    is_verified = models.BooleanField(default=False)
    
    def __unicode__(self):
        return self.network_id
        
    # get the display name for a social network
    def _get_network_name(self):
        for k,v in NETWORK_IDS:
            if k == self.network_id:
                return v
        else:
            return None
    profile_name = property(_get_network_name)

    # get the url for a social network with the username/id inserted
    def _get_profile_url(self):
        try:
            return NETWORK_URLS[self.network_id] % str(self.username)
        except:
            return None
    profile_url = property(_get_profile_url)


class InstantMessengerProfile(models.Model):
    user = models.ForeignKey(User, db_index=True, related_name='instant_messenger_profiles')
    messenger_id = models.CharField(max_length=16, choices=MESSENGER_IDS, db_index=True)
    username = models.CharField(max_length=64)
    date_added = models.DateTimeField(_('date added'), auto_now_add=True)
    date_verified = models.DateTimeField(_('date verified'), default=datetime.now)
    is_verified = models.BooleanField(default=False)
    
    def __unicode__(self):
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
    profile_name = property(_get_messenger_name)

    # get the url to start a chat with the username/id provided
    def _get_messenger_url(self):
        try:
            return MESSENGER_URLS[self.messenger_id] % str(self.username)
        except:
            return None
    messenger_url = property(_get_messenger_url)

        
class WebsiteProfile(models.Model):
    user = models.ForeignKey(User, db_index=True, related_name='website_profiles')
    name = models.CharField(max_length=64)
    url = models.URLField(verify_exists=True)
    date_added = models.DateTimeField(_('date added'), auto_now_add=True)
    date_verified = models.DateTimeField(_('date verified'), default=datetime.now)
    is_verified = models.BooleanField(default=False)
    
    def __unicode__(self):
        return self.url

    # get the display name for a website
    def _get_website_name(self):
        return self.name
    profile_name = property(_get_website_name)