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
             return redirect("/home")

        else:
            error_message = "用户名或者密码错误"

    return render(request, "login.html", {"error_message": error_message})

USER_LIST = [
    {'username':'zhangsan', 'age':'23', 'gender':'male'},
]

for i in range(1,10):
    temp = {'username':'zhangsan', 'age':'23', 'gender':'male'}
    USER_LIST.append(temp)
def home(request):
    if request.method == "POST":
        username = request.POST.get('username')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        temp = {'username':username, 'age':age, 'gender':gender}
        USER_LIST.append(temp)
    return render(request,'home.html' ,{'user_list':USER_LIST})