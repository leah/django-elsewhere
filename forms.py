from django import forms

from psn.models import *
from psn.util import NETWORK_IDS, MESSENGER_IDS

class SocialNetworkSettingsForm(forms.Form):
    form_name = forms.CharField(widget=forms.HiddenInput(), initial='sn_form')
    network_id = forms.ChoiceField(choices=NETWORK_IDS)
    username = forms.CharField(max_length=32)

class InstantMessengerSettingsForm(forms.Form):
    form_name = forms.CharField(widget=forms.HiddenInput(), initial='im_form')
    messenger_id = forms.ChoiceField(choices=MESSENGER_IDS)
    username = forms.CharField(max_length=32)
        
class WebsiteSettingsForm(forms.Form):
    form_name = forms.CharField(widget=forms.HiddenInput(), initial='w_form')
    name = forms.CharField(max_length=32)
    url = forms.URLField(max_length=250, initial='http://')