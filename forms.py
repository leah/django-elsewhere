from django import newforms as forms
from django.http import Http404

from django_psn.models import *
from django_psn.util import NETWORK_IDS, MESSENGER_IDS

class SocialNetworkSettingsForm(forms.Form):
    form_name = forms.CharField(widget=forms.HiddenInput(), initial='sn_form')
    network_id = forms.ChoiceField(choices=NETWORK_IDS)
    username = forms.CharField(max_length=32)

    def __init__(self, user, *args, **kwargs):
        try:
            self.user = user
        except:
            raise Http404
        super(SocialNetworkSettingsForm, self).__init__(*args, **kwargs)
        
    def save(self, new_data):
        profile = SocialNetworkProfile(user=self.user, network_id=new_data['network_id'], username=new_data['username'])
        profile.save()
        return profile

class InstantMessengerSettingsForm(forms.Form):
    form_name = forms.CharField(widget=forms.HiddenInput(), initial='im_form')
    messenger_id = forms.ChoiceField(choices=MESSENGER_IDS)
    username = forms.CharField(max_length=32)
    
    def __init__(self, user, *args, **kwargs):
        try:
            self.user = user
        except:
            raise Http404
        super(InstantMessengerSettingsForm, self).__init__(*args, **kwargs)
        
    def save(self, new_data):
        profile = InstantMessengerProfile(user=self.user, messenger_id=new_data['messenger_id'], username=new_data['username'])
        profile.save()
        return profile
        
class WebsiteSettingsForm(forms.Form):
    form_name = forms.CharField(widget=forms.HiddenInput(), initial='w_form')
    name = forms.CharField(max_length=32)
    url = forms.URLField(max_length=250, initial='http://')
    
    def __init__(self, user, *args, **kwargs):
        try:
            self.user = user
        except:
            raise Http404
        super(WebsiteSettingsForm, self).__init__(*args, **kwargs)
        
    def save(self, new_data):
        profile = WebsiteProfile(user=self.user, name=new_data['name'], url=new_data['url'])
        profile.save()
        return profile