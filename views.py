from django.http import HttpResponse, HttpResponseServerError, Http404
from django.template import RequestContext
from django.contrib.auth import SESSION_KEY
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response

from psn.elsewhere import PortableProfile
from psn.models import *
from psn.forms import *

# portable social networks
@login_required
def social_networks(request):
    
    # get the logged-in user from the session
    u_id = request.session.get(SESSION_KEY)
    try:
        u = User.objects.get(id=u_id)
    except:
        raise Http404
    
    if request.method == 'POST':
        # delete a profile
        new_data = request.POST.copy()
        try:
            form_name = new_data['form_name']
            delete_id = new_data['delete_id']
            if form_name == 'delete_sn_form':
                profile = u.social_network_profiles.get(id=delete_id)
            if form_name == 'delete_im_form':
                profile = u.instant_messenger_profiles.get(id=delete_id)
            if form_name == 'delete_w_form':
                profile = u.website_profiles.get(id=delete_id)
            profile.delete()
        except:
            pass

    return render_to_response('psn.html', {
        'social_network_profiles': u.social_network_profiles.all(),
        'instant_messenger_profiles': u.instant_messenger_profiles.all(),
        'website_profiles': u.website_profiles.all(),
    }, context_instance=RequestContext(request))

# portable social networks settings page
@login_required
def settings_social_networks(request):
    errormsg = statusmsg = ""
    new_data = {}
    
    # get the logged-in user from the session
    u_id = request.session.get(SESSION_KEY)
    try:
        u = User.objects.get(id=u_id)
    except:
        raise Http404
    
    # create blank forms
    sn_form = SocialNetworkSettingsForm(u)
    im_form = InstantMessengerSettingsForm(u)
    w_form = WebsiteSettingsForm(u)

    if request.method == 'POST':
        new_data = request.POST.copy()
        form_name = new_data['form_name']
        if form_name == 'sn_form':
            sn_form = SocialNetworkSettingsForm(u, new_data)
            if sn_form.is_valid():
                sn_form.save(new_data)
                sn_form = SocialNetworkSettingsForm(u) # new form
                statusmsg = "Your social network profile settings were successfully updated!"
            else:
                errormsg = "Please correct the errors below."
        elif form_name == 'im_form':
            im_form = InstantMessengerSettingsForm(u, new_data)
            if im_form.is_valid():
                im_form.save(new_data)
                im_form = InstantMessengerSettingsForm(u) # new form
                statusmsg = "Your instant messenger profile settings were successfully updated!"
            else:
                errormsg = "Please correct the errors below."
        elif form_name == 'w_form':
            w_form = WebsiteSettingsForm(u, new_data)
            if w_form.is_valid():
                w_form.save(new_data)
                w_form = WebsiteSettingsForm(u) # new form
                statusmsg = "Your website profile settings were successfully updated!"
            else:
                errormsg = "Please correct the errors below."
        else:
            # wtf?
            return HttpResponseServerError

    return render_to_response('psn_settings.html', {
        'sn_form': sn_form, 'im_form': im_form, 'w_form': w_form,
        'errormsg': errormsg, 'statusmsg': statusmsg,
    }, context_instance=RequestContext(request))

def elsewhere_info(request):
    if request.method != 'GET':
        return HttpResponseServerError

    # Find the requested user        
    if 'id' in request.GET:
        try:
            u = User.objects.get(id=request.GET['id'])
        except:
            raise Http404('Invalid id: %s' % request.GET['id'])
    elif 'ident' in request.GET:
        try:
            u = User.objects.get(username__exact=request.GET['ident'])
        except:
            raise Http404('Invalid ident: %s' % request.GET['ident'])
    else:
        raise Http404("Must specify user id as 'id' or username as 'ident'.")
        
    profile = PortableProfile(u)
    
    # Friend graph edges are returned by default.
    # To ignore the graph edges, there is an optional request param want_edges=0
    want_edges = True
    try:
        if 'want_edges' in request.GET and int(request.GET['want_edges']) == 0:
            want_edges = False
    except:
        pass
    
    if want_edges:
        # Provide custom code here to set the edges in / edges out for your
        # site's friend relationships
        edges_in = []
        profile.edges_in = edges_in
        
        edges_out = []
        profile.edges_out = edges_out
    
    # return the profile data as JSON
    json = profile.get_json(want_edges)
    return HttpResponse(json)