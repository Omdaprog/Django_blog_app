from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post, Comment
from blog.forms import PostForm, CommentForm ,UserForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
# Create your views here.


def post_list(request):
    posts = Post.objects.filter(published_date__lte= timezone.now()).order_by('-published_date')
    stuff_for_frontend = {'posts':posts}
    return render(request,'blog/post_list.html', stuff_for_frontend)


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid(): 
            comment = form.save(commit=False)                # commit=False it's mean that dont save the form in database
            comment.author = form.save(commit=False) 
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else: 
        form = CommentForm()
    stuff_for_frontend = {'post':post,
                          'form': form}
    return render (request, 'blog/post_detail.html', stuff_for_frontend)

@login_required
def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('post_draft_list')
    else: 
        form = PostForm()
        stuff_for_frontend = {'form': form}
    return render(request, 'blog/post_edit.html', stuff_for_frontend)

@login_required
def post_Edit(request ,pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST or None, request.FILES or None ,instance=post )
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
        stuff_for_frontend = {'form': form, 'post':post}
    
    return render(request, 'blog/post_edit.html',stuff_for_frontend) 

@login_required
def post_draft_list(request):
    posts = Post.objects.filter(published_date__isnull=True).order_by('-created_date')
    stuff_for_frontend = {'posts':posts}
    return render (request, 'blog/draft_list.html', stuff_for_frontend)

@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_list')



@login_required
def remove_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('post_detail', pk=comment.post.pk)

@login_required
def remove_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('/')


@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('post_detail', pk=comment.post.pk)


def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(**form.cleaned_data)
            login(request, new_user)
            return redirect('/')
    else:
        form = UserForm()
    return render(request, 'registration/signup.html', {'form':form})








