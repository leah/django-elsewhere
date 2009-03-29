django-elsewhere - Social Network Links for Django
===================================

Formerly Django-PSN (Portable Social Networks) and originally created for Pownce.

Authors:
------------
* [Leah Culver] (http://leahculver.com)
* [Chris Drackett] (http://chrisdrackett.com/)
* Please send feedback to leah@sixapart.com


Install:
------------

1. You can get the source directly from GitHub either by downloading the project or checking out the repository: 'git clone git://github.com/leah/django-elsewhere.git'

2. After checking the project out, add the 'elsewhere' directory to your Python path.

3. Once the project is on your python path, add 'elsewhere' to your INSTALLED_APPS in settings.py.

4. run python manage.py syncdb from within your project to add the elsewhere database tables and initial data.

About:
------------

Django-elsewhere allows users of a website to provide and display information about their 
other online social networks. The project was created to let Pownce users 
show their friends what other online social networks they participate in. 
The hyperlinks to other profiles make use of the XFN rel="me" standard [http://www.gmpg.org/xfn/] (http://www.gmpg.org/xfn/), 
which enables auto-discovery of social network profiles which the user has chosen to consolidate 
into a single identity.


Dependencies:
------------

* Django 1.0
* Django Contrib Auth, place 'django.contrib.auth' in INSTALLED_APPS setting


To use the sample views:
------------------------

Add the following to your urlconf:

	(r'^elsewhere/', include('elsewhere.urls'))

For sample templates add the path to elsewhere/templates to your TEMPLATE_DIRS setting.


To use the icons:
------------------------

Each profile object has an icon property that will render the icon while in DEBUG mode.
Just use:

    {{ profile.icon }}

To enable the icons in production, you'll need to point your webserver to the icon directory.
The default path to an icon is like: /elsewhere/img/vox.png


About the models:
-----------------

For Django-elsewhere, the online profiles have been divided into three categories:

* Social Networks (online social site profiles)
* Instant Messengers (screennames)
* Websites (can be used for other types of online profiles such as weblogs or OpenID providers)

You can create and edit these either in the Django admin or using Django forms.


Using a different list of profiles:
------------------------

You can define your own list of available social networks and instant messengers by adding SOCIAL_NETWORKS
and/or INSTANT_MESSENGERS lists to your settings:

    SOCIAL_NETWORKS = [
        {
            'id': 'facebook',
            'name': 'Facebook',
            'url': 'http://www.facebook.com/profile.php?id=%s',
            'identifier': 'User ID',
            'icon': 'facebook.png',
        },
        {
            'id': 'myspace',
            'name': 'MySpace',
            'url': 'http://www.myspace.com/%s',
            'identifier': 'Username',
            'icon': 'myspace.png',
        },
    ]

    INSTANT_MESSENGERS = [
        {
            'id': 'aim',
            'name': 'AIM',
            'url': 'aim:goim?screenname=%s',
            'icon': 'aim.png',
        },
        {
            'id': 'yahoo',
            'name': 'Y!',
            'url': 'ymsgr:sendim?%s',
            'icon': 'yahoo.png',
        },
    ]

If no SOCIAL_NETWORKS or INSTANT_MESSENGERS are defined in your project settings, django-elsewhere will
default to using the lists in fatty_lists.py.

Other resources:
----------------

* [Portable Social Networks for Django] (http://leahculver.com/2007/09/03/portable-social-networks-for-django/) - Leah Culver
* [Thoughts on the Social Graph] (http://bradfitz.com/social-graph-problem/) - Brad Fitzpatrick and David Recordon
* [Microformats Social Network Portability] (http://microformats.org/wiki/social-network-portability) - from the Microformats wiki
* [XHTML Friends Network] (http://www.gmpg.org/xfn/)
* [Building Blocks for Portable Social Networks] (http://www.brianoberkirch.com/2007/08/08/building-blocks-for-portable-social-networks/) - Brian Oberkirch
* [Following Friends Across Walled Gardens] (http://www.personalinfocloud.com/2006/11/following_frien.html) - Thomas Vander Wal
* [Open Social Graph @ Plaxo] (http://www.plaxo.com/info/opensocialgraph) - identity consolidation tools