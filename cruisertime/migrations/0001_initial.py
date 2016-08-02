# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-02 04:27
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Meetup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meet_date', models.DateField(default=datetime.date(2016, 8, 1))),
                ('meet_time', models.TimeField(default=b'21:27:04')),
                ('location_name', models.CharField(choices=[('Lift', (('BR', 'Brooks'), ('HGS', 'Hogsback'), ('SKY', 'Skyline Express'), ('DSY', 'Daisy'), ('KRS', 'Kehrs Chair'), ('TYE', 'Tye Mill'), ('DD', 'Double Diamond'), ('7H', '7th Heaven'), ('JUP', 'Jupiter Express'), ('SCR', 'Southern Cross'), ('RT', 'Rope Tow'))), ('Base Area', (('GPL', 'Granite Peaks Lodge'), ('TCL', 'Tye Creek Lodge'), ('PCL', 'Pacific Crest Lodge'), ('FG', 'The Foggy Goggle'), ('BTP', 'Bulls Tooth Pub'), ('SP', 'Ski Patrol Shed'), ('CHK', 'Ski Check'), ('SKOO', 'Ski School Shed'), ('MNT', 'Vehicle Maintenance Shed'))), ('Cabins', (('PRK', 'Cabin Parking Lot'), ('TRL', 'Cabin Trail Entrance'), ('BSC', 'Ski Cruiser Cabin'), ('PNG', 'Penguin Cabin'), ('EVT', 'Everett Cabin'), ('SWS', 'Swiss Cabin'), ('MT', 'Moutaineer Cabin')))], default='BR', max_length=200)),
                ('lift_terminal', models.CharField(blank=True, choices=[('TOP', 'Top'), ('BOT', 'Bottom')], default=' ', max_length=200)),
                ('notes_text', models.CharField(default="Let's meetup!", max_length=200)),
                ('meet_name', models.CharField(default='New Meetup', max_length=200)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('lon', models.FloatField(default='-121.086300')),
                ('lat', models.FloatField(default='47.734230')),
            ],
        ),
    ]