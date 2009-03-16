from django.http import HttpResponse, HttpResponseRedirect, HttpResponseServerError, Http404
from django.template import RequestContext
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response

from elsewhere.profile import PortableProfile
from elsewhere.models import *
from elsewhere.forms import *


@login_required
def example(request):
    
    # create blank forms
    sn_form = SocialNetworkSettingsForm()
    im_form = InstantMessengerSettingsForm()
    w_form = WebsiteSettingsForm()

    if request.method == 'POST':
        new_data = request.POST.copy()
        form_name = new_data['form_name']
        # Add forms
        if form_name == 'sn_form':
            sn_form = SocialNetworkSettingsForm(new_data)
            if sn_form.is_valid():
                profile = SocialNetworkProfile(user=request.user, network_id=sn_form.cleaned_data['network_id'], username=sn_form.cleaned_data['username'])
                profile.save()
                return HttpResponseRedirect(request.path)
        elif form_name == 'im_form':
            im_form = InstantMessengerSettingsForm(new_data)
            if im_form.is_valid():
                profile = InstantMessengerProfile(user=request.user, messenger_id=im_form.cleaned_data['messenger_id'], username=im_form.cleaned_data['username'])
                profile.save()
                return HttpResponseRedirect(request.path)
        elif form_name == 'w_form':
            w_form = WebsiteSettingsForm(new_data)
            if w_form.is_valid():
                profile = WebsiteProfile(user=request.user, name=w_form.cleaned_data['name'], url=w_form.cleaned_data['url'])
                profile.save()
                return HttpResponseRedirect(request.path)
        # Delete forms
        elif form_name == 'delete_sn_form':
            request.user.social_network_profiles.get(id=request.POST['delete_id']).delete()
            return HttpResponseRedirect(request.path)
        elif form_name == 'delete_im_form':
            request.user.instant_messenger_profiles.get(id=request.POST['delete_id']).delete()
            return HttpResponseRedirect(request.path)
        elif form_name == 'delete_w_form':
            request.user.website_profiles.get(id=request.POST['delete_id']).delete()
            return HttpResponseRedirect(request.path)
        # WTF?
        else:
            return HttpResponseServerError

    return render_to_response('elsewhere/example.html', {
        'sn_form': sn_form, 'im_form': im_form, 'w_form': w_form,
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