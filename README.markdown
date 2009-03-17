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

You can get the source directly from GitHub either by downloading the project or checking out the repository.

A quick shortcut is to checkout the project directly into your Python path:

	git clone git://github.com/leah/django-elsewhere.git elsewhere


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


About the models:
-----------------

For Django-elsewhere, the online profiles have been divided into three categories:

* Social Networks (online social site profiles)
* Instant Messengers (screennames)
* Websites (can be used for other types of online profiles such as weblogs or OpenID providers)

You can create and edit these either in the Django admin or using Django forms.


Other resources:
----------------

* [Portable Social Networks for Django] (http://leahculver.com/2007/09/03/portable-social-networks-for-django/) - Leah Culver
* [Thoughts on the Social Graph] (http://bradfitz.com/social-graph-problem/) - Brad Fitzpatrick and David Recordon
* [Microformats Social Network Portability] (http://microformats.org/wiki/social-network-portability) - from the Microformats wiki
* [XHTML Friends Network] (http://www.gmpg.org/xfn/)
* [Building Blocks for Portable Social Networks] (http://www.brianoberkirch.com/2007/08/08/building-blocks-for-portable-social-networks/) - Brian Oberkirch
* [Following Friends Across Walled Gardens] (http://www.personalinfocloud.com/2006/11/following_frien.html) - Thomas Vander Wal
* [Open Social Graph @ Plaxo] (http://www.plaxo.com/info/opensocialgraph) - identity consolidation tools