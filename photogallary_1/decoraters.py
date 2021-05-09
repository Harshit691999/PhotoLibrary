from django.http import HttpResponse
from django.shortcuts import redirect

def check_authenticated(view_fun):
    def wrapper_fun(request,*args, **kwargs):
        if request.user.is_authenticated:
            return redirect('userpage')
        else:
            return view_fun(request,*args, **kwargs)
    return wrapper_fun