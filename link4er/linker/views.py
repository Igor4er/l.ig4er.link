from django.http import HttpResponseRedirect, HttpResponseNotFound
from .models import RedirectLink

def redirection(request, redirect):
    try:
        rl = RedirectLink.objects.get(redirect=redirect)
    except:
        return HttpResponseRedirect('/')
    return HttpResponseRedirect(rl.to)
