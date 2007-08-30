from django import template
from django_psn.util import get_network_name, get_profile_url, get_messenger_name

register = template.Library()

@register.filter
# get the display name for a social network
def network_name(network_id):
    return get_network_name(network_id)
        
@register.filter
# get the url for a social network with the username/id inserted
def profile_url(network_id, username):
    return get_profile_url(network_id, username)

@register.filter
# get the display name for an IM service
def messenger_name(messenger_id):
    return get_messenger_name(messenger_id)