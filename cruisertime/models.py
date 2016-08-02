from __future__ import unicode_literals
from django.db import models
from django.forms import ModelForm
from django.utils import timezone
#from django.contrib.gis.db import models
from django.core.exceptions import ValidationError
from django import forms
import datetime
import time
from django.utils.timezone import utc

# include your models here 

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

# model classes
class Meetup(models.Model):
    meet_date = models.DateField(auto_now=False, auto_now_add=False, default=datetime.date.today())
    meet_time = models.TimeField(auto_now=False, auto_now_add=False, default=datetime.datetime.now().strftime('%H:%M:%S'))
    location_name = models.CharField(max_length=200, choices=LOCATION_CHOICES, default="BR")
    lift_terminal = models.CharField(max_length=200, blank=True, choices=TERMINAL_CHOICES, default=" ")
    notes_text = models.CharField(max_length=200, default="Let's meetup!")
    meet_name = models.CharField(max_length=200, default="New Meetup")	
    create_date = models.DateTimeField(auto_now_add=True)
    lon = models.FloatField(default='-121.086300')
    lat = models.FloatField(default='47.734230')
    #mpoly = models.PointField()  # GeoDjango-specific: a geometry field (PointField)
    def __str__(self):
        return self.meet_name


#class WorldBorder(models.Model):            
#    name = models.CharField(max_length=50)
#    area = models.IntegerField()
#    pop2005 = models.IntegerField('Population 2005')
#    fips = models.CharField('FIPS Code', max_length=2)
#    iso2 = models.CharField('2 Digit ISO', max_length=2)
#    iso3 = models.CharField('3 Digit ISO', max_length=3)
#    un = models.IntegerField('United Nations Code')
#    region = models.IntegerField('Region Code')
#    subregion = models.IntegerField('Sub-Region Code')
#    lon = models.FloatField()
#    lat = models.FloatField()
#    mpoly = models.MultiPolygonField()  # GeoDjango-specific: a geometry field (MultiPolygonField), The default spatial reference system for geometry fields is WGS84 (SRID is 4326)
#    def __str__(self):              # __unicode__ on Python 2
#        return self.name
        
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
    def clean_meet_date(self):
        date = self.cleaned_data['meet_date']
        if date < datetime.date.today():
            raise ValidationError("The date cannot be in the past!")
        return date