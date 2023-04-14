from django.http import HttpResponseRedirect
from .models import RedirectLink

def redirection(request, redirect):
    rl = RedirectLink.objects.get(redirect=redirect)
    return HttpResponseRedirect(rl.to)
