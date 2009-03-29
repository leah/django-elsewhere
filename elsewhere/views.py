from django.http import HttpResponse, HttpResponseRedirect, HttpResponseServerError
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response

from elsewhere.models import *


@login_required
def example(request):
    if request.method == 'POST':

        new_data = request.POST.copy()

        # Add forms
        if new_data.get('sn-form') or new_data.get('im-form') or new_data.get('w-form'):

            if new_data.get('sn-form'):
                form = SocialNetworkForm(new_data)
            elif new_data.get('im-form'):
                form = InstantMessengerForm(new_data)
            elif new_data.get('w-form'):
                form = WebsiteForm(new_data)

            if form.is_valid():
                profile = form.save(commit=False)
                profile.user = request.user
                profile.save()
                return HttpResponseRedirect(request.path)
            else:
                ## TODO should probably show the errors
                print form.errors

        # Delete forms
        elif new_data.get('delete-sn-form') or new_data.get('delete-im-form') or new_data.get('delete-w-form'):
            delete_id = request.POST['delete_id']

            if new_data.get('delete-sn-form'):
                request.user.social_network_profiles.get(id=delete_id).delete()
            elif new_data.get('delete-im-form'):
                request.user.instant_messenger_profiles.get(id=delete_id).delete()
            elif new_data.get('delete-w-form'):
                request.user.website_profiles.get(id=delete_id).delete()

            return HttpResponseRedirect(request.path)

        # WTF?
        else:
            return HttpResponseServerError

    # Create blank forms
    sn_form = SocialNetworkForm()
    im_form = InstantMessengerForm()
    w_form = WebsiteForm()

    return render_to_response('elsewhere/example.html', {
        'sn_form': sn_form, 'im_form': im_form, 'w_form': w_form,
    }, context_instance=RequestContext(request))