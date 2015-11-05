from django.conf.urls import url
from . import views

urlpatterns = [
            url(r'^$', views.index, name='index'),
            url(r'^(?P<pk>.+)/confirm/$', views.confirm, name = 'confirm'),
            url(r'^(?P<pk>.+)/$', views.survey, name='survey'),
            ]
