from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from .forms import TaskForm
from .models import Task

def all_posts(request):
    posts = Task.objects.all()
    context = {'posts': posts}
    return render(request, 'man/index.html', context)

def post_by_id(request, id):
    post = Task.objects.get(id=id)
    context = {'id': id, 'post': post}
    return render(request, 'man/post.html', context=context)

@csrf_exempt
def create_post(request: HttpRequest):
    if request.method == 'POST':
        form = TaskForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('man')
    else:
        form = TaskForm()
    context = {'form': form}
    return render(request, 'man/post-form.html', context)

@csrf_exempt
def update_post(request: HttpRequest, id):
    post = Task.objects.get(id=id)
    if request.method == 'POST':
        form = TaskForm(data=request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('man')
    else:
        form = TaskForm(instance=post)
    context = {'form': form}
    return render(request, 'man/post-form.html', context)

@csrf_exempt
def delete_post(request, id):
    post = Task.objects.get(id=id)
    if request.method == 'POST':
        post.delete()
        return redirect('man')
    context = {'post': post}
    return render(request, 'man/delete-post.html', context)
