from django.contrib import admin

from elsewhere.models import *

class ProfileAdmin(admin.ModelAdmin):
    raw_id_fields = ['user']

class SocialNetworkProfileAdmin(ProfileAdmin):
    list_display = ('user', 'network', 'username') #, 'date_added')

class InstantMessengerProfileAdmin(ProfileAdmin):
    list_display = ('user', 'network', 'username') #, 'date_added')

class WebsiteProfileAdmin(ProfileAdmin):
    list_display = ('user', 'name', 'url') #, 'date_added')

## TODO Not sure why I can't grab date_added from the parent Profile model, need to figure this out.

admin.site.register(Network)
admin.site.register(SocialNetworkProfile, SocialNetworkProfileAdmin)
admin.site.register(WebsiteProfile, WebsiteProfileAdmin)
admin.site.register(InstantMessengerProfile, InstantMessengerProfileAdmin)