from django.db import models
from django.urls import reverse
from django.db.models import UniqueConstraint # Constrains fields to unique values
from django.db.models.functions import Lower # Returns lower cased value of field
from django.conf import settings

class Venue(models.Model):
    name = models.CharField('Venue Name', max_length=120)
    address = models.CharField(max_length=300)
    zip_code = models.CharField('Zip Code', max_length=15)
    phone = models.CharField('Contact Number', max_length=25, blank=True)
    web = models.URLField('Website Address', blank=True)
    # organization = models.ForeignKey(Organization, on_delete=models.SET_NULL, null=True, blank=True, related_name='venues')

    # Methods
    def get_absolute_url(self):
        """Returns the URL to access a particular instance of MyModelName."""
        return reverse('venue-detail', args=[str(self.id)])

    def __str__(self):
        return self.name

class Organization(models.Model):
    # Core Identification
    name = models.CharField(max_length=255)
    legal_name = models.CharField(max_length=255, blank=True)
    tax_id = models.CharField('Tax/VAT ID', max_length=50, unique=True)
    description = models.TextField(blank=True)
    
    # # Contact & Location
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    website = models.URLField(blank=True)
    address = models.TextField()
    
    # # Classification
    # BUSINESS_TYPES = [
    #     ('CORP', 'Corporation'),
    #     ('LLC', 'Limited Liability Company'),
    #     ('SOLE', 'Sole Proprietorship'),
    # ]
    # structure = models.CharField(max_length=4, choices=BUSINESS_TYPES)
    
    # Metadata
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Organizations"
    
    def get_absolute_url(self):
        """Returns the URL to access a particular instance of MyModelName."""
        return reverse('organization-detail', args=[str(self.id)])

    def __str__(self):
        return self.name

class Event(models.Model):
    """A typical class defining a model, derived from the Model class."""

    # Fields
    # my_field_name = models.CharField(max_length=20, help_text='Enter field documentation')
    name = models.CharField(max_length=100, help_text='Make it catchy!')
    description = models.TextField(help_text='Be sure to include any description already on event imaage.')
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(null=True, blank=True)
    location_note = models.CharField(max_length=200,blank=True)
    cancelled = models.BooleanField(default=False)

    ### Example of linking the event to a sponsoring organization and a location
    location = models.ForeignKey(Venue, on_delete=models.SET_NULL, null=True, blank=True, related_name='managed_events')
    # Example of a many-to-many relationship
    sponsor = models.ManyToManyField(Organization, related_name='sponsoring_events', blank=True)
    followers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='followed_events', blank=True)

    # Metadata
    class Meta:
        ordering = ['start_time']
        permissions = (("can_mark_cancelled", "Set event as cancelled"),)

    # Methods
    def get_absolute_url(self):
        """Returns the URL to access a particular instance of MyModelName."""
        return reverse('event-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.name
    




