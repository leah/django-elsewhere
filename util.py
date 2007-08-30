NETWORK_IDS = (
    ('43things', '43Things'),
    ('bebo', 'Bebo'),
    ('catster', 'Catster'),
    ('delicious', 'del.icio.us'),
    ('digg', 'Digg'),
    ('dodgeball', 'Dodgeball'),
    ('dogster', 'Dogster'),
    ('dopplr', 'Dopplr'),
    ('facebook', 'Facebook'),
    ('flickr', 'Flickr'),
    ('goodreads', 'GoodReads'),
    ('hi5', 'Hi5'),
    ('jaiku', 'Jaiku'),
    ('lastfm', 'Last.fm'),
    ('linkedin', 'LinkedIn'),
    ('lj', 'LiveJournal'),
    ('mog', 'MOG'),
    ('multiply', 'Multiply'),
    ('myspace', 'MySpace'),
    ('newsvine', 'Newsvine'),
    ('ning', 'Ning'),
    ('orkut', 'Orkut'),
    ('pandora', 'Pandora'),
    ('pownce', 'Pownce'),
    ('reddit', 'Reddit'),
    ('sonicliving', 'SonicLiving'),
    ('stumbleupon', 'StumbleUpon'),
    ('tabblo', 'Tabblo'),
    ('tagworld', 'TagWorld'),
    ('technorati', 'Technorati'),
    ('tribe', 'Tribe'),
    ('twitter', 'Twitter'),
    ('upcoming', 'Upcoming'),
    ('vox', 'Vox'),
    ('youtube', 'YouTube'),
    ('zooomr', 'Zooomr'),
)

NETWORK_URLS = {
    '43things':'http://www.43things.com/person/%s/',
    'bebo':'http://www.bebo.com/Profile.jsp?MemberId=%s',
    'catster':'http://www.catster.com/cats/%s',
    'delicious':'http://del.icio.us/%s/',
    'digg':'http://digg.com/users/%s/',
    'dodgeball':'http://www.dodgeball.com/user?uid=%s',
    'dogster':'http://www.dogster.com/dogs/%s',
    'dopplr':'http://www.dopplr.com/traveller/%s/',
    'facebook':'http://www.facebook.com/profile.php?id=%s',
    'flickr':'http://flickr.com/photos/%s/',
    'goodreads':'http://www.goodreads.com/user/show/%s',
    'hi5':'http://hi5.com/friend/profile/displayProfile.do?userid=%s',
    'jaiku':'http://%s.jaiku.com/',
    'lastfm':'http://www.last.fm/user/%s/',
    'linkedin':'http://www.linkedin.com/in/%s',
    'lj':'http://%s.livejournal.com/',
    'mog':'http://mog.com/%s',
    'multiply':'http://%s.multiply.com/',
    'myspace':'http://www.myspace.com/%s',
    'newsvine':'http://%s.newsvine.com/',
    'ning':'http://%s.ning.com/',
    'orkut':'http://www.orkut.com/Profile.aspx?uid=%s',
    'pandora':'http://pandora.com/people/%s',
    'pownce':'http://pownce.com/%s/',
    'reddit':'http://reddit.com/user/%s/',
    'sonicliving':'http://www.sonicliving.com/user/%s/',
    'stumbleupon':'http://%s.stumbleupon.com/',
    'tabblo':'http://www.tabblo.com/studio/person/%s/',
    'tagworld':'http://www.tagworld.com/%s',
    'technorati':'http://technorati.com/people/technorati/%s',
    'tribe':'http://people.tribe.net/%s',
    'twitter':'http://twitter.com/%s',
    'upcoming':'http://upcoming.yahoo.com/user/%s',
    'vox':'http://%s.vox.com/',
    'youtube':'http://www.youtube.com/user/%s',
    'zooomr':'http://www.zooomr.com/photos/%s',
}

MESSENGER_IDS = (
    ('aim', 'AIM'),
    ('msn', 'MSN Messenger'),
    ('yahoo', 'Yahoo! Messenger'),
    ('gtalk', 'GTalk'),
    ('icq', 'ICQ'),
    ('skype', 'Skype'),
    ('jabber', 'Jabber'),
)

# get the display name for a social network
def get_network_name(network_id):
    for k,v in NETWORK_IDS:
        if k == network_id:
            return v
    else:
        return None

# get the url for a social network with the username/id inserted
def get_profile_url(network_id, username):
    try:
        return NETWORK_URLS[network_id] % str(username)
    except:
        return None

# get the display name for an IM service
def get_messenger_name(messenger_id):
    for k, v in MESSENGER_IDS:
        if k == messenger_id:
            return v
    else:
        return messenger_id