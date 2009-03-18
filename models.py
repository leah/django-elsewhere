from datetime import datetime

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
from django.contrib import admin

from elsewhere import sn_manager, im_manager

GOOGLE_PROFILE_URL = 'http://www.google.com/s2/favicons?domain_url=%s'


class Profile:
    """ Base class for converting raw profile data to objects. """

    data_manager = None

    def _get_data_item(self, profile_id):
        # Find profile data for this profile id
        for network in self.data_manager.data:
            if network['id'] == profile_id:
                return network
        return None

    def _get_name(self):
        # Profile display name
        return self.data_item['name']
    name = property(_get_name)

    def _get_url(self):
        # Profile URL with username
        return self.data_item['url'] % self.username
    url = property(_get_url)
    
    def _get_icon_name(self):
        # Icon name
        return self.data_item['icon']
    icon_name = property(_get_icon_name)

    def _get_icon(self):
        # Icon URL or link to Google icon service
        if self.icon_name:
            return reverse('elsewhere_img', args=[self.icon_name])
        return GOOGLE_PROFILE_URL % self.url
    icon = property(_get_icon)


class SocialNetworkProfile(models.Model, Profile):

    data_manager = sn_manager

    user = models.ForeignKey(User, db_index=True, related_name='social_network_profiles')
    network_id = models.CharField(max_length=16, choices=data_manager.choices, db_index=True)
    username = models.CharField(max_length=64)
    date_added = models.DateTimeField(_('date added'), auto_now_add=True)
    date_verified = models.DateTimeField(_('date verified'), default=datetime.now)
    is_verified = models.BooleanField(default=False)
    
    def __unicode__(self):
        return self.network_id

    def get_data_item(self):
        return self._get_data_item(self.network_id)
    data_item = property(get_data_item)


class InstantMessengerProfile(models.Model, Profile):

    data_manager = im_manager

    user = models.ForeignKey(User, db_index=True, related_name='instant_messenger_profiles')
    messenger_id = models.CharField(max_length=16, choices=data_manager.choices, db_index=True)
    username = models.CharField(max_length=64)
    date_added = models.DateTimeField(_('date added'), auto_now_add=True)
    date_verified = models.DateTimeField(_('date verified'), default=datetime.now)
    is_verified = models.BooleanField(default=False)

    def __unicode__(self):
        return self.username

    def get_data_item(self):
        return self._get_data_item(self.messenger_id)
    data_item = property(get_data_item)


class WebsiteProfile(models.Model):
    user = models.ForeignKey(User, db_index=True, related_name='website_profiles')
    name = models.CharField(max_length=64)
    url = models.URLField(verify_exists=True)
    date_added = models.DateTimeField(_('date added'), auto_now_add=True)
    date_verified = models.DateTimeField(_('date verified'), default=datetime.now)
    is_verified = models.BooleanField(default=False)

    def __unicode__(self):
        return self.url

    def _get_icon(self):
        # No known icons! Just return the Google service URL.
        return GOOGLE_PROFILE_URL % self.url
    icon = property(_get_icon)