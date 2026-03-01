from django import forms

from .models import Event

class FollowEventForm(forms.Form):
    # This field will be hidden
    user_id = forms.IntegerField(widget=forms.HiddenInput(), initial=123)
    event_id = forms.IntegerField(widget=forms.HiddenInput())
    
class UnfollowEventForm(forms.Form):
    # This field will be hidden
    user_id = forms.IntegerField(widget=forms.HiddenInput(), initial=123)
    event_id = forms.IntegerField(widget=forms.HiddenInput())