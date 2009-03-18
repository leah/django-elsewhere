from django import forms
from elsewhere import sn_manager, im_manager

class SocialNetworkSettingsForm(forms.Form):
    form_name = forms.CharField(widget=forms.HiddenInput(), initial='sn_form')
    network_id = forms.ChoiceField(choices=sn_manager.choices)
    username = forms.CharField(max_length=32)

class InstantMessengerSettingsForm(forms.Form):
    form_name = forms.CharField(widget=forms.HiddenInput(), initial='im_form')
    messenger_id = forms.ChoiceField(choices=im_manager.choices)
    username = forms.CharField(max_length=32)
        
class WebsiteSettingsForm(forms.Form):
    form_name = forms.CharField(widget=forms.HiddenInput(), initial='w_form')
    name = forms.CharField(max_length=32)
    url = forms.URLField(max_length=250, initial='http://')