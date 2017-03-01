# -*- coding:gbk -*-
from django.shortcuts import render, redirect
from django.contrib import auth
from django.core.context_processors import csrf
from .forms import MyRegistrationForm
from django.core.urlresolvers import reverse


def login(request):
    c = {}
    c.update(csrf(request))
    return render(request, 'auth/login.html', c)


def auth_view(request):
    username = request.POST.get('username', '')   #if no username then ''
    password = request.POST.get('password', '')
    
    #if exists (uname,pwd), return a User Object, else return None
    user = auth.authenticate(username=username, password=password)

    if user:
        auth.login(request, user)
        return redirect('/accounts/loggedin') #redirect after POST
    else:
        return redirect('/accounts/invalid')


def loggedin(request):
    return render(request, 'auth/loggedin.html', 
                  {'full_name': request.user.username})


def invalid_login(request):
    return render(request, 'auth/invalid_login.html', )


def logout(request):
    auth.logout(request)
    return render(request, 'auth/logout.html')


def register_user(request):

    if request.method == 'POST':
        form = MyRegistrationForm(request.POST)   
        if form.is_valid():
            form.save() 
            url = reverse('rss_feed.views.register_success', kwargs={'username': form.cleaned_data['username']})
            return redirect(url)
    
 
    args = {}
    args.update(csrf(request))
    args['form'] = MyRegistrationForm()
    return render(request, 'auth/register.html', args)


def register_success(request, username):
    return render(request, "auth/register_success.html", {'username': username})
