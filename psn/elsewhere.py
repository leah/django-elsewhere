from django.utils import simplejson

'''
    PortableProfile
    
    Represents a person's profile as defined by the elsewhere_info file.
    This data can be used to recognized claimed and/or verified identities
    and recognize user relationships based on inbound and outbound edges.
    
    To generate a JSON response, create a view which creates a PortableProfile
    with user data and returns the get_json string for that profile.
'''
class PortableProfile(object):
    user = None
    node_id = None
    node_ident = ''
    node_type = 'person'
    edges_out = []
    edges_in = []
    is_verified_mbox = False
    
    def __init__(self, user):
        self.user = user
        self.node_id = user.id
        self.node_ident = user.username
    
    def __str__(self):
        return '%s: %s' % (str(self.node_id), str(self.node_ident))
    
    def _get_mbox_sha1sum(self):
        import sha
        return sha.new('mailto:%s' % self.user.email).hexdigest()
    mbox_sha1sum = property(_get_mbox_sha1sum)
    
    def _get_claimed_urls(self):   
        claimed_urls = []
        # http://facebook.com/profile?id=23423434
        for sn in self.user.social_network_profiles.all():
            if not sn.is_verified:
                claimed_urls.append(sn.profile_url)
        # aim:bradfitzpatrick
        for im in self.user.instant_messenger_profiles.all():
            if not im.is_verified:
                claimed_urls.append('%s:%s' % (im.messenger_id, im.username))
        # http://bradfitz.com/
        for w in self.user.website_profiles.all():
            if not w.is_verified:
                claimed_urls.append(w.url)
        # if the email is unverified, include it in the claimed urls
        if not self.is_verified_mbox:
            claimed_urls.append('mbox_sha1sum:%s' % self.mbox_sha1sum)
        return claimed_urls
    claimed_urls = property(_get_claimed_urls)

    def _get_verified_urls(self):   
        verified_urls = []
        # http://facebook.com/profile?id=23423434
        for sn in self.user.social_network_profiles.all():
            if sn.is_verified:
                verified_urls.append(sn.profile_url)
        # aim:bradfitzpatrick
        for im in self.user.instant_messenger_profiles.all():
            if im.is_verified:
                verified_urls.append('%s:%s' % (im.messenger_id, im.username))
        # http://bradfitz.com/
        for w in self.user.website_profiles.all():
            if w.is_verified:
                verified_urls.append(w.url)
        return verified_urls
    verified_urls = property(_get_verified_urls)
    
    def get_json(self, want_edges=True):
        # unordered dict of profile data
        profile_data = {
            'node_id': self.node_id,
            'node_ident': self.node_ident,
            'node_type': self.node_type,
        }
        if self.is_verified_mbox and self.mbox_sha1sum:
            profile_data['mbox_sha1sum'] = self.mbox_sha1sum
        if self.claimed_urls:
            profile_data['claimed_urls'] = self.claimed_urls
        if self.verified_urls:
            profile_data['verified_urls'] = self.verified_urls
        if want_edges:
            if self.edges_out:
                profile_data['edges_out'] = self.edges_out 
            if self.edges_in:
                profile_data['edges_in'] = self.edges_in
        return simplejson.dumps(profile_data)