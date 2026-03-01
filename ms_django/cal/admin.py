from django.contrib import admin

from .models import Venue, Organization, Event

admin.site.register(Venue)
admin.site.register(Organization)
admin.site.register(Event)