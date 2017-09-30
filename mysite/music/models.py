from django.db import models
#from django.core.urlresolvers import reverse
from django.urls import reverse


class Album(models.Model):
    artist = models.CharField(default="none", null=True, max_length=250)
    album_title = models.CharField(default="none", null=True, max_length=250)
    genre = models.CharField(default="none", null=True, max_length=100)
    album_logo = models.CharField(default="none", null=True, max_length=1000)
    
    # Teaching model where to find its detail page
    def get_absolute_url(self):
        print("using get_absolute_url")
        print("primary key is", self.pk)
        return reverse('music:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.album_title + ' - ' + self.artist   ###prettier return of object


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)  ### delete Song if its Album is deleted
    ### foreignKey is a way of saying "object that i may not know about now but trust me i will upon creation!", in this case, an album
    file_type = models.CharField(max_length=10)
    song_title = models.CharField(max_length=20)
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.song_title
