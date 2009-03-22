from elsewhere.default_list import *
from elsewhere.models import SocialNetwork, InstantMessenger

# this function will fill the database with default data (stored in fatty_lists.py)

def fill_db():
    '''This is a function so it doesn't get called automatically on import; 
    instead it's called at the end of urls.py, but could potentially be called
    from anywhere that gets read in only once.'''

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