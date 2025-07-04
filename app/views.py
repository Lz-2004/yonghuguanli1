from django.http import HttpResponse
from django.shortcuts import render, redirect

def index(request):
    return HttpResponse("Hello app")

def login(request):
    error_message =' '
    if request.method == "POST":
        username = request.POST.get('username',None)
        password = request.POST.get('password',None)

        if username == 'root' and password == '123':
             return redirect('https://app7119.acapp.acwing.com.cn/')

        else:
            error_message = "用户名或者密码错误"

    return render(request, "login.html", {"error_message": error_message})
