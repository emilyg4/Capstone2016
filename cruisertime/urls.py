from django.conf.urls import url

from . import views

# include your urls here
app_name = 'cruisertime'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^meetcreate', views.meetcreate, name='meetcreate'),
    url(r'^get_meetform', views.get_meetform, name='get_meetform'),
    url(r'^meetdetail', views.meetdetail, name='meetdetail'),
    url(r'^meetattend', views.meetattend, name='meetattend'),
    url(r'^about', views.about, name='about'),
]
