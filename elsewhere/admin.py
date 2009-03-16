from django.contrib import admin
from elsewhere import models

class ProfileAdmin(admin.ModelAdmin):
    raw_id_fields = ['user']

class SocialNetworkProfileAdmin(ProfileAdmin):
    list_display = ('user', 'network_id', 'username',)

class InstantMessengerProfileAdmin(ProfileAdmin):
    list_display = ('user', 'messenger_id', 'username',)

class WebsiteProfileAdmin(ProfileAdmin):
    list_display = ('user', 'name', 'url',)

admin.site.register(models.SocialNetworkProfile, SocialNetworkProfileAdmin)
admin.site.register(models.WebsiteProfile, WebsiteProfileAdmin)
admin.site.register(models.InstantMessengerProfile, InstantMessengerProfileAdmin)