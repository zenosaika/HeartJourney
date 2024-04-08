from django.shortcuts import render, redirect
from .models import Blog
from .forms import BlogForm
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

def get_blog(req, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(req, 'Blog/blog.html', {'blog': blog})

@login_required
def create_blog(req):
    if req.method == 'POST':
        form = BlogForm(req.POST, req.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = req.user
            form.save()
            return redirect('/')
    return render(req, 'Blog/new_blog.html', {'form': BlogForm()})

@login_required
def edit_blog(req, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    if req.method == 'POST':
        form = BlogForm(req.POST, req.FILES, instance=blog)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = req.user
            form.save()
            return redirect(f'/blog/{blog_id}')
    return render(req, 'Blog/edit_blog.html', {'form': BlogForm(instance=blog), 'blog': blog})

@login_required
def delete_blog(req, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    if req.method == 'POST':
        confirm_text = req.POST.get('confirm_text')
        if confirm_text == blog.title:
            blog.delete()
            return redirect('/')
    return render(req, 'Blog/delete_blog.html', {'blog': blog})
