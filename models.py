from datetime import datetime

from django import forms
from django.db import models
from django.core.cache import cache
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
from django.contrib import admin

GOOGLE_PROFILE_URL = 'http://www.google.com/s2/favicons?domain_url=%s'

class Network(models.Model):
    """ Model for storing networks. """

    name = models.CharField(max_length=100)
    url = models.URLField()
    identifier = models.CharField(max_length=100)
    icon = models.CharField(max_length=100, blank=True)

    class Meta:
        abstract = True

    def __unicode__(self):
        return self.name

## TODO the full SocialNetwork and InstantMessenger lists should probably be cached.

class SocialNetwork(Network):
    class Meta:
        verbose_name_plural = 'social networks'

class InstantMessenger(Network):
    class Meta:
        verbose_name_plural = 'instant messanger networks'

class Profile(models.Model):
    """ Common profile functions. """

    date_added = models.DateTimeField(_('date added'), auto_now_add=True)
    date_verified = models.DateTimeField(_('date verified'), default=datetime.now)
    is_verified = models.BooleanField(default=False)

    class Meta:
        abstract = True

    def _get_name(self):
        # Profile display name
        return self.network.name
    name = property(_get_name)

    def _get_url(self):
        # Profile URL with username
        return self.network.url
    url = property(_get_url)
    
    def _get_icon_name(self):
        # Icon name
        return self.network.icon
    icon_name = property(_get_icon_name)

    def _get_icon(self):
        # Icon URL or link to Google icon service
        if self.icon_name:
            return reverse('elsewhere_img', args=[self.icon_name])
        return GOOGLE_PROFILE_URL % self.url
    icon = property(_get_icon)


class SocialNetworkProfile(Profile):
    user = models.ForeignKey(User, db_index=True, related_name='social_network_profiles')
    network = models.ForeignKey(SocialNetwork, db_index=True)
    username = models.CharField(max_length=64)
    
    def __unicode__(self):
        return self.network_id

class SocialNetworkForm(forms.ModelForm):

    class Meta:
        model = SocialNetworkProfile
        fields = ('network', 'username')


class InstantMessengerProfile(Profile):
    user = models.ForeignKey(User, db_index=True, related_name='instant_messenger_profiles')
    network = models.ForeignKey(InstantMessenger, db_index=True)
    username = models.CharField(max_length=64)

    def __unicode__(self):
        return self.username

class InstantMessengerForm(forms.ModelForm):

    class Meta:
        model = InstantMessengerProfile
        fields = ('network', 'username')


class WebsiteProfile(models.Model):
    user = models.ForeignKey(User, db_index=True, related_name='website_profiles')
    name = models.CharField(max_length=64)
    url = models.URLField(verify_exists=True)

    def __unicode__(self):
        return self.url

    def _get_icon(self):
        # No known icons! Just return the Google service URL.
        return GOOGLE_PROFILE_URL % self.url
    icon = property(_get_icon)


class WebsiteForm(forms.ModelForm):

    class Meta:
        model = WebsiteProfile
        fields = ('name', 'url')