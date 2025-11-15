from django.shortcuts import render, redirect, get_object_or_404, HttpResponse

from .models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login , logout
from django.contrib import messages


def register_view(request):
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            messages.success(request, "Registration successful!")
            return redirect('post_list')
    else:
        messages.success(request, "Registration unsuccessful!")
        form = UserCreationForm()
    return render(request ,'register.html', {'form': form})

def login_view(request):
    
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "login successful!")
            print(' user is logged in successfully')
            return redirect('post_list')
    else:
        messages.success(request, "login unsuccessful!")
        form = AuthenticationForm()
    return render(request, 'login.html',{'form':form})
        
def logout_view(request):
    logout(request)
    return redirect('login')

@login_required   
def post_list(request):
    post = Post.objects.filter(user=request.user)
    return render(request,'post_list.html',{'post':post})

@login_required
def post_create(request):
    
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'post_form.html',{'form':form})
            
            
            
@login_required
def post_delete(request):
    
    post = get_object_or_404(Post,id = id, user = request.user)
    
    if request.method == 'POST':
        post.delete()
        return redirect('post_list')
    
    return render(request,'post_delete.html', {'post': post})





