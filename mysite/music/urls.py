from django.conf.urls import url    ###import url object!
from . import views                 ###views.py from in our directory

### namespacing to use in templates
app_name = 'music'

urlpatterns = [
        # /music
        url(r'^$', views.IndexView.as_view(), name='index'),

        # /music/<song_id>/favorite/
        ###url(r'^(?P<album_id>[0-9]+)/favorite$', views.favorite, name='favorite'),
        
        url(r'album/add/$', views.AlbumCreate.as_view(), name='album-add'),

        # /music/<album.id>
        url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
        
        url(r'album/(?P<pk>[0-9]+)$', views.AlbumUpdate.as_view(), name='album-update'),

        url(r'album/(?P<pk>[0-9]+)/delete/$', views.AlbumDelete.as_view(), name='album-delete'),
        ]
