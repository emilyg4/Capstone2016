"""
Definition of models.
"""
from __future__ import unicode_literals
from django.db import models
from django.forms import ModelForm
from django.utils import timezone
from django.core.exceptions import ValidationError
from django import forms
import datetime
import time
from django.utils.timezone import utc

# query lists
LOCATION_CHOICES = (
    ('Lift', (
        ('BR', 'Brooks'),
        ('HGS', 'Hogsback'),
        ('SKY', 'Skyline Express'),
        ('DSY', 'Daisy'),
        ('KRS', 'Kehrs Chair'),
        ('TYE', 'Tye Mill'),
        ('DD', 'Double Diamond'),
        ('7H', '7th Heaven'),
        ('JUP', 'Jupiter Express'),
        ('SCR', 'Southern Cross'),
        ('RT', 'Rope Tow'),
        )
    ),
    ('Base Area', (
        ('GPL', 'Granite Peaks Lodge'),
        ('TCL', 'Tye Creek Lodge'),
        ('PCL', 'Pacific Crest Lodge'),
        ('FG', 'The Foggy Goggle'),
        ('BTP', 'Bulls Tooth Pub'),
        ('SP', 'Ski Patrol Shed'),
        ('CHK', 'Ski Check'),
        ('SKOO', 'Ski School Shed'),
        ('MNT', 'Vehicle Maintenance Shed'),
        )
    ),
    ('Cabins', (
        ('PRK', 'Cabin Parking Lot'),
        ('TRL', 'Cabin Trail Entrance'),
        ('BSC', 'Ski Cruiser Cabin'),
        ('PNG', 'Penguin Cabin'),
        ('EVT', 'Everett Cabin'),
        ('SWS', 'Swiss Cabin'),
        ('MT', 'Moutaineer Cabin'),
        )
    ),
)

TERMINAL_CHOICES = (
    ('TOP', 'Top'),
    ('BOT', 'Bottom'),
)

def IsLiftLocation(locationName):
    for locationTypeKey, locationListVal in LOCATION_CHOICES:
        if locationTypeKey == 'Lift':
            for key, val in locationListVal:
                if key == locationName:
                    return True
    return False

# model classes
class Meetup(models.Model):
    meet_date = models.DateField(auto_now=False, auto_now_add=False, default=datetime.date.today())
    meet_time = models.TimeField(auto_now=False, auto_now_add=False, default=datetime.datetime.now().strftime('%H:%M:%S'))
    lift_terminal = models.CharField(max_length=200, blank=True, choices=TERMINAL_CHOICES)
    location_name = models.CharField(max_length=200, choices=LOCATION_CHOICES)
    notes_text = models.CharField(max_length=200, default="Let's meetup!")
    meet_name = models.CharField(max_length=200, default="New Meetup")	
    create_date = models.DateTimeField(auto_now_add=True)
    lon = models.FloatField(default='-121.086300')
    lat = models.FloatField(default='47.734230')
    #mpoly = models.PointField()  # GeoDjango-specific: a geometry field (PointField)
    def __str__(self):
        return self.meet_name
        
# ModelForm classes
class MeetupForm(ModelForm):
    class Meta:
        error_css_class = 'error'
        required_css_class = 'required'
        model = Meetup
        widgets = {
            'lat': forms.HiddenInput(), 
            'lon': forms.HiddenInput(),
            'meet_date': forms.DateInput(attrs={'class':'datepicker'}),
            }
        fields = ['meet_date', 'meet_time', 'location_name', 'meet_name', 'lift_terminal', 'notes_text', 'lat', 'lon']
    def clean_lift_terminal(self):
        location = self.data.get('location_name')
        terminal = self.cleaned_data['lift_terminal']
        if (IsLiftLocation(location)):
            if not terminal:
                raise ValidationError("Location is a lift. Must supply Terminal.")
        return terminal
    #def clean(self):
    #    cleaned_data = super(MeetupForm, self).clean()
    #    location = cleaned_data['location_name']
    #    terminal = cleaned_data['lift_terminal']
    #    #do your cleaning here
    #    if (IsLiftLocation(location)):
    #        if not terminal:
    #            raise ValidationError("Location is a lift. Must supply Terminal.")
    #    return cleaned_data
    def clean_meet_date(self):
        date = self.cleaned_data['meet_date']
        if date < datetime.date.today():
            raise ValidationError("The date cannot be in the past!")
        return date