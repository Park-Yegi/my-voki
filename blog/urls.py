from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^otherevent$', views.otherevent, name='otherevent'),
    url(r'^notice$', views.notice, name='notice'),
    url(r'^freeboard$', views.freeboard, name='freeboard'),
    url(r'^sinbang$', views.sinbang, name='sinbang'),
    url(r'^gayo$', views.gayo, name='gayo'),
    url(r'^kapo$', views.kapo, name='kapo'),
    url(r'^timetable$', views.timetable, name='timetable'),
    url(r'^streaming$', views.streaming, name='streaming'),
    url(r'^listenagain$', views.listenagain, name='listenagain'),
    url(r'^songrequest$', views.songrequest, name='songrequest'),
    url(r'^news$', views.news, name='news'),
    url(r'^drama$', views.drama, name='drama'),
    url(r'^vokintro$', views.vokintro, name='vokintro'),
    url(r'^hello$', views.hello, name='hello'),
    url(r'^history$', views.history, name='history'),
    url(r'^memberintro$', views.memberintro, name='memberintro'),
    url(r'^contact$', views.contact, name='contact'),
    url(r'^register$', views.register, name='register'),
    url(r'^login$', views.login, name='login'),
    url(r'^post/(?P<pk>\d+)/remove/$', views.post_remove, name='post_remove'),
]