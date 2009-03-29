from django.db.models import signals

from elsewhere.default_list import *
from elsewhere.models import SocialNetwork, InstantMessenger

# this function will fill the database with default data (stored in default_lists.py)

def fill_db(sender=None, **kwargs):
    for item in default_social_networks: # fill social networks
        if item.has_key('identifier'):
            ident = item['identifier']
        else:
            ident = ''

        SocialNetwork.objects.get_or_create(name=item['name'], defaults={
            'url': item['url'],
            'identifier': ident,
            'icon': item['icon']
        })

    for item in default_im_networks: # fill IM networks
        if item.has_key('identifier'):
            ident = item['identifier']
        else:
            ident = ''

        InstantMessenger.objects.get_or_create(name=item['name'], defaults={
            'url': item['url'],
            'identifier': ident,
            'icon': item['icon']
        })

signals.post_syncdb.connect(fill_db)