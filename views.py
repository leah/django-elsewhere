from django.http import HttpResponse, HttpResponseRedirect, HttpResponseServerError
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response

from elsewhere.models import *
from elsewhere.forms import *


@login_required
def example(request):

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
    else:
        # Create blank forms
        sn_form = SocialNetworkSettingsForm()
        im_form = InstantMessengerSettingsForm()
        w_form = WebsiteSettingsForm()

    return render_to_response('elsewhere/example.html', {
        'sn_form': sn_form, 'im_form': im_form, 'w_form': w_form,
    }, context_instance=RequestContext(request))