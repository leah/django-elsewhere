Portable Social Networks for Django
===================================

django-psn - Portable Social Networks for Django
_Leah Culver (leahculver.com)_
_Please send feedback to leah@sixapart.com_

Django-PSN provides users of a social website to provide and display information about their 
other online social networks. The project was created to let Pownce users 
show their friends what other online social networks they participate in. 
The hyperlinks to other profiles make use of the XFN rel="me" standard (http://www.gmpg.org/xfn/), 
which enables auto-discovery of social network profiles which the user has chosen to consolidate 
into a single identity. Hopefully it's also parsable by Plaxo's Online Identity Consolidator (http://www.plaxo.com/info/opensocialgraph).

In addition, Django-PSN provides a JSON response with the user's claimed URLs and friend/fan relationships 
(represented as user ids for graph edges in and edges out). An example can be found at /interface/elsewhere_info 
with params id=user_id or indent=username.

I copied this format from LiveJournal, guessing that it will be copied by other websites as well. 
I'm open to changing this format and updating Django-PSN accordingly. This data can 
be used to connect friends across online social networks, building a free social graph.

Dependencies:
------------

* Django development version (Djang-PSN is now tracking the Django Trunk.)
* Django Auth Module, place 'django.contrib.auth' in INSTALLED_APPS setting


To use psn:
-----------

1. Rename django-psn 'psn'.
2. Make sure the 'psn' folder is available on your python path.
3. Add 'psn' to your INSTALLED_APPS setting.
4. To create the necessary database tables, run the command: python manage.py syncdb

To use the sample views:
------------------------
Add the following to your urlconf:

	(r'^social_networks/$', 'psn.views.social_networks'),
	(r'^settings/social_networks/$', 'psn.views.settings_social_networks'),

For sample templates add the path to psn/templates to your TEMPLATE_DIRS setting.

About the models:
-----------------

There are two chunks of information considered interesting to social network portability:
		
Edges In and Edges Out - These define 'friend' relationships between users.
Claimed and Verified URLs - Assertions of a user's identity in other social networks.
		
Edges In and Out is application specific but fairly easy data to obtain for a site owner.
		
Identity URL assertions can be obtained through a GUI which can be mutually interesting to 
users and interesting to data collectors. Daniel Burka (Pownce designer) and I spent a lot of time thinking of how to gather these 
assertions from users. We decided that while online identities take one form to a data collector 
(a profile URL), users perceive online identity in three forms:

* Social Networks (online social site profiles)
* Instant Messengers (screenname)
* Websites (can be used for other types of online profiles such as weblogs or OpenID providers)

We really wanted Pownce users to get immediate positive feedback for providing Pownce with their online identities. 
Pownce users are not only contributing to social graph data, but are also displaying links 
and profile data on their application profiles for their friends.

Generate elsewhere_info JSON:
Add the following to your urlconf:

	(r'^interface/elsewhere_info/$', 'psn.views.elsewhere_info'),

Customize the elsewhere_info view in psn/views.py. Specifically, you will need to 
generate lists of edges in and edges out based on how your application handles friend relationships.
		
Expected Request for elsewhere_info
		
Given a numeric node id or node identifier, return JSON about the
user, optionally with all related edges.

GET /interface/elsewhere_info?id=234234		# unique userid
GET /interface/elsewhere_info?ident=brad	# unique identifier (username / group name)
Host: www.elsewhere-cooperating-site.com

arguments:
id=			 # integer nodeid to query.	 this or 'ident' is required.
ident=		 # string identifier to query.	this or 'id' is required.
want_edges=1	 # optional: explicitly request/don't request edges_{in,out} (default whatever you want)

Expected Response for elsewhere_info

	HTTP 200 OK
	Content-Type: text/json		 # server isn't picky; can be whatever

	{
	"node_id": 239847283947,
	"node_ident": "brad",
	"node_type": {"person"|"group"|"openid"},
	"mbox_sha1sum": "f1d2d2f924e986ac86fdf7b36c94bcdf32beec15",	 # of "mailto:email@foo.com", ONLY IF email is verified

	"claimed_urls": [
	 "mbox_sha1sum:f1d2d2f924e986ac86fdf7b36c94bcdf32beec15", # if not verified.
	 "http://facebook.com/profile?id=23423434",
	 "aim:bradfitzpatrick",
	 "http://bradfitz.com/",
	],

	"verified_urls": [	 # ONLY if proven with OpenID / facebook auth, etc...
	 "http://facebook.com/profile?id=23423434",
	}

	"edges_out" : [	 # all edges out, whether dest nodes are people _or_ groups.
	  1,
	  2,
	  5,
	  10,
	],
	"edges_in":[   # all edges out, whether source nodes are people _or_ groups.
	  8,
	],
	};

Other resources:
----------------

* Thoughts on the Social Graph (http://bradfitz.com/social-graph-problem/) - Brad Fitzpatrick and David Recordon
* Microformats Social Network Portability (http://microformats.org/wiki/social-network-portability) - from the Microformats wiki
* XHTML Friends Network (http://www.gmpg.org/xfn/)
* Building Blocks for Portable Social Networks (http://www.brianoberkirch.com/2007/08/08/building-blocks-for-portable-social-networks/) - Brian Oberkirch
* Following Friends Across Walled Gardens (http://www.personalinfocloud.com/2006/11/following_frien.html) - Thomas Vander Wal
* Open Social Graph @ Plaxo (http://www.plaxo.com/info/opensocialgraph) - identity consolidation tools