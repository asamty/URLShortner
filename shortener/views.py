from django.shortcuts import render
from shortener.models import Shortener
from .forms import ShortenerForm
from django.http import HttpResponseRedirect, Http404

def index(request):
    template = 'index.html'
    context = {}
    context['form'] = ShortenerForm()

    if request.method == 'GET':
        return render(request, template, context)

    elif request.method == 'POST':

        shortener_form = ShortenerForm(request.POST)

        if shortener_form.is_valid():
            
            shortened_object = shortener_form.save() #getting info from entered record

            new_url = request.build_absolute_uri('/') + shortened_object.short_code #making shortened url
            
            original_url = shortened_object.original_url
             
            context['new_url']  = new_url
            context['original_url'] = original_url
            context['short_code'] = shortened_object.short_code
             
            return render(request, template, context)

        context['errors'] = shortener_form.errors

        return render(request, template, context)

def redirect_url_view(request, short_url):
    """
    Function to redirect to original link
    """
    try:
        shortener = Shortener.objects.get(short_code=short_url)
        shortener.count += 1        
        shortener.save()
        
        return HttpResponseRedirect(shortener.original_url)
        
    except:
        raise Http404('Sorry, this link is broken')

def counter_view(request, short_url):
    """
    Function to get statistics for link (number of redirects from shortened url)
    """
    shortener = Shortener.objects.get(short_code=short_url)
    counter = shortener.count
    new_url = request.build_absolute_uri('/') + short_url
    original_url = shortener.original_url
    

    return render(request,'counter.html',{'counter': counter, 'new_url': new_url, 'original_url': original_url})