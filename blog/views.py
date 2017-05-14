from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from .models import Post
from .forms import PostForm

def register(request):
    return render(request, 'blog/register.html')
def login(request):
    return render(request, 'blog/login.html')

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.hits = post.hits + 1
    post.save()
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')

def otherevent(request):
    return render(request, 'blog/otherevent.html')

def notice(request):
    posts = Post.objects.filter(published_date__lte=timezone.now(), type='notice').order_by('-published_date')
    return render(request, 'blog/notice.html', {'posts': posts})

def freeboard(request):
    posts = Post.objects.filter(published_date__lte=timezone.now(), type='freeboard').order_by('-published_date')
    return render(request, 'blog/freeboard.html', {'posts': posts})

def sinbang(request):
    return render(request, 'blog/sinbang.html')

def gayo(request):
    return render(request, 'blog/gayo.html')

def kapo(request):
    return render(request, 'blog/kapo.html')

def timetable(request):
    return render(request, 'blog/timetable.html')

def streaming(request):
    return render(request, 'blog/streaming.html')

def listenagain(request):
    return render(request, 'blog/listenagain.html')

def songrequest(request):
    return render(request, 'blog/songrequest.html')

def news(request):
    return render(request, 'blog/news.html')

def drama(request):
    return render(request, 'blog/drama.html')

def vokintro(request):
    return render(request, 'blog/vokintro.html')

def hello(request):
    return render(request, 'blog/hello.html')

def history(request):
    return render(request, 'blog/history.html')

def memberintro(request):
    return render(request, 'blog/memberintro.html')

def contact(request):
    return render(request, 'blog/contact.html')



