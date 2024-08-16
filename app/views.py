from django.shortcuts import render
from django.views.generic.edit import CreateView, DeleteView
from .models import Post, Review
from django.urls import reverse_lazy
from .forms import CreatePostForm
from django.contrib.contenttypes.models import ContentType



def home(request):
    posts=Post.objects.all()
    return render(request, 'home.html', context= {'posts':posts})

class CreatePost(CreateView):
    model = Post
    success_url = reverse_lazy('home')
    template_name = 'create.html'
    form_class = CreatePostForm

class DeletePost(DeleteView):
    model = Post
    success_url = reverse_lazy('home')
    template_name = 'delete.html'


def create_review(request):
    reviews=Review.objects.all()

    if request.method == 'POST':
        text = request.POST.get('text', None)
        post_id = request.POST.get('post_id', None)
        Review.objects.create(text=text, content_type=ContentType.objects.get_for_model(Post),
                              object_id = int(post_id))
        return render(request, 'coment.html', {'reviews': reviews})

    return render(request, 'coment.html', context= {'reviews':reviews})