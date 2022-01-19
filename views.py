from django.shortcuts import render,redirect
from .models import short_urls
from .forms import UrlForm
from .shortner import shortner

# Create your views here.
def Home(request, token):
    long_url = short_urls.objects.filter(short_url=token)[0]
    return redirect(long_url.long_url)

            

    return render(request, 'home.html', {'form': form, 'a': a})