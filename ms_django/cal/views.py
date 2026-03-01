from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse

from .models import Event, Venue, Organization
from .forms import FollowEventForm

def index(request):
    
    class EventListView(generic.ListView,LoginRequiredMixin):
        model = Event
        context_object_name = 'event_list'
        ordering = ['start_time']
    
    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 0)
    num_visits += 1
    request.session['num_visits'] = num_visits
    

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context={'event_list': Event.objects.all(), 'num_visits': num_visits})

def organizations(request):
    
    class OrganizationListView(generic.ListView):
        model = Organization
        context_object_name = 'organization_list'
        ordering = ['name']
    

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'organizations.html', context={'organization_list': Organization.objects.all()})

class EventsFollowedByUserListView(LoginRequiredMixin,generic.ListView):
    """Generic class-based view listing events followed by current user."""
    model = Event
    template_name = 'cal/myevents.html'
    paginate_by = 10

    def get_queryset(self):
        return (
            Event.objects.filter(followers=self.request.user)
            .order_by('start_time')
        )

class EventDetailView(generic.DetailView):
    model = Event
    context_object_name = 'event'

class OrganizationDetailView(generic.DetailView):
    model = Organization
    context_object_name = 'organization'

def follow_event(request, pk):
    # Ensure the request is a POST request for safety
    if request.method == 'POST':
        instance = get_object_or_404(Event, pk=pk)
        # Update the specific field(s)
        instance.followers.add(request.user)
        instance.save()
        # Redirect the user back to the previous page or a success page
        return redirect('event-detail', pk=pk)
    else:
        # Optional: return an error for GET requests
        return HttpResponseNotAllowed(['POST'])

def unfollow_event(request, pk):
    # Ensure the request is a POST request for safety
    if request.method == 'POST':
        instance = get_object_or_404(Event, pk=pk)
        # Update the specific field(s)
        instance.followers.remove(request.user)
        instance.save()
        # Redirect the user back to the previous page or a success page
        return redirect('event-detail', pk=pk)
    else:
        # Optional: return an error for GET requests
        return HttpResponseNotAllowed(['POST'])

