from django.http import HttpResponse, HttpResponseRedirect
from django.core.context_processors import csrf
from django.shortcuts import render_to_response, redirect
from testblog.models import Comments, Posts
from django.contrib import auth
from django.contrib.auth.models import User 
from testblog.forms import UserLoginForm, RegisterForm, PostForm, CommentForm, ChangeProfile
from django.views.generic.simple import direct_to_template
from django.contrib.auth.forms import UserCreationForm
from django.forms import forms
from django.template import loader, Context 
from django.forms.models import inlineformset_factory
from django.contrib.auth.views import login, logout

def main(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/')
    post = Posts.objects.all().order_by('-date_post')
    comment = Comments.objects.all()
    return render_to_response('main.html', locals()) 

def myposts(request, id):
    post = Posts.objects.all()
    return render_to_response('myposts.html', locals())

def profile(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/')
    #user = User.objects.all()
    #post = Posts.objects.filter(user_id = id)
    return render_to_response('profile.html', locals())

def view_post(request, id):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/')
    post1 = Posts.objects.get(id = id)
    comment = Comments.objects.filter(post_id = id).order_by('-date_com')
    form = CommentForm()
    if request.method == 'POST':
        user = request.user
        u = Comments(user_id=user, post_id = post1)
        form = CommentForm(request.POST, instance=u)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/main")
    return render_to_response('post1.html', locals())
 
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect("/profile")
        else:
            return HttpResponseRedirect("/")
    return render_to_response('login.html', locals())

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/")

def register(request):
    form = RegisterForm()
    if request.method == 'POST':
        data = request.POST.copy()
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save(data)          
            return HttpResponseRedirect("/")
    else:
        form = RegisterForm()
    return render_to_response("registration/register.html", locals())

def addpost(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/')
    form = PostForm()
    if request.method == 'POST':      
        user = request.user
        post = Posts(user_id=user)
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()           
            return HttpResponseRedirect('/profile/%s/myposts' % request.user.id)
    else:
        form = PostForm()
    return render_to_response("postadd.html", locals())

def changeprofile(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/')
    form = ChangeProfile()
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        change = User.objects.filter(id = request.user.id).update(first_name=first_name, last_name=last_name, email=email)
        return HttpResponseRedirect('/profile')
    return render_to_response("changeprofile.html", locals())
