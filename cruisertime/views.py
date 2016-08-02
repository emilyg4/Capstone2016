"""
Definition of views.
"""
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import Meetup, MeetupForm
from django.template import loader

# include your views here
def index(request):
    return render(request, 'cruisertime/index.html')

def get_meetform(request):
    return render(request, 'cruisertime/get_meetform.html')

def about(request):
    return render(request, 'cruisertime/about.html')

def meetdetail(request):
    latest_meetup_list = Meetup.objects.order_by('-create_date')[:1]
    upcoming_meetup_list = Meetup.objects.order_by('meet_date')[:5]
    template = loader.get_template('cruisertime/meetdetail.html')
    context = {
        'latest_meetup_list':latest_meetup_list,
        'upcoming_meetup_list':upcoming_meetup_list
    }
    return render(request, 'cruisertime/meetdetail.html', context)

def meetattend(request):
    #latest_meetup_list = Meetup.objects.order_by('-create_date')[:1]
    upcoming_meetup_list = Meetup.objects.order_by('meet_date')[:5]
    all_meetups = Meetup.objects.all()
    template = loader.get_template('cruisertime/meetattend.html')
    context = {
        #'latest_meetup_list':latest_meetup_list,
        'upcoming_meetup_list':upcoming_meetup_list,
        'all_meetups':all_meetups
    }
    return render(request, 'cruisertime/meetattend.html', context)


def meetcreate(request):
    if request.method == 'POST':                    # if this is a POST request, process the form data
        form = MeetupForm(request.POST)
        if form.is_valid():                  # check whether it's valid and process the data in form.cleaned_data as required
            new_meetup = form.save(commit=False)             # create a form instance and populate it with data from the request:
            # modify in some way (location)
            #m = Meetup.objects.get(pk=1)
            #f = MeetupForm(request.POST, instance=m)
            form.save()                      
            return HttpResponseRedirect('meetdetail') # redirect to a new URL
    else:                                           # if a GET (or any other method) we'll create a blank form
        form = MeetupForm()
    return render(request, 'cruisertime/get_meetform.html', {'meetup_form': form})



#from django.shortcuts import render
#from django.http import HttpRequest
#from django.template import RequestContext
#from datetime import datetime

#def home(request):
#    """Renders the home page."""
#    assert isinstance(request, HttpRequest)
#    return render(
#        request,
#        'app/index.html',
#        context_instance = RequestContext(request,
#        {
#            'title':'Home Page',
#            'year':datetime.now().year,
#        })
#    )

#def contact(request):
#    """Renders the contact page."""
#    assert isinstance(request, HttpRequest)
#    return render(
#        request,
#        'app/contact.html',
#        context_instance = RequestContext(request,
#        {
#            'title':'Contact',
#            'message':'Your contact page.',
#            'year':datetime.now().year,
#        })
#    )

#def about(request):
#    """Renders the about page."""
#    assert isinstance(request, HttpRequest)
#    return render(
#        request,
#        'app/about.html',
#        context_instance = RequestContext(request,
#        {
#            'title':'About',
#            'message':'Your application description page.',
#            'year':datetime.now().year,
#        })
#    )
