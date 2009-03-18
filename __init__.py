# Profile options can be overridden by project settings
try:
    from settings import SOCIAL_NETWORKS
except ImportError:
    from fatty_lists import SOCIAL_NETWORKS
try:
    from settings import INSTANT_MESSENGERS
except ImportError:
    from fatty_lists import INSTANT_MESSENGERS


class ProfileManager:
    """ Handle raw data for lists of profiles."""
    data = {}

    def _get_choices(self):
        """ List of choices for profile select fields. """
        return [(props['id'], props['name']) for props in self.data]
    choices = property(_get_choices)


class SocialNetworkManager(ProfileManager):

    data = SOCIAL_NETWORKS

sn_manager = SocialNetworkManager()


class InstantMessengerManager(ProfileManager):

    data = INSTANT_MESSENGERS

im_manager = InstantMessengerManager()