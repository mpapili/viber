from django.views import generic
from .models import Album
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

class IndexView(generic.ListView):
    template_name = 'music/index.html'
    context_object_name = 'all_albums'
    
    def get_queryset(self):
        return Album.objects.all()
    
class DetailView(generic.DetailView):
    model = Album
    template_name = 'music/detail.html'
    
class AlbumCreate(CreateView):
    model = Album
    print("running album create")
    template_name = 'music/album_form.html'
    fields=['artist', 'album_title', 'genre', 'album_logo']
    
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        #self.object.post_date = datetime.now()
        return super(AlbumCreate, self).form_valid(form)

class AlbumUpdate(UpdateView):
    model = Album
    fields=['artist', 'album_title', 'genre', 'album_logo']
    
class AlbumDelete(DeleteView):
    model= Album
    success_url = reverse_lazy('music:index')

