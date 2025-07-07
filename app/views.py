from http.client import responses

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
    {'id':0, 'username':'zhangsan', 'age':'23', 'gender':'male', 'email':'289460@qq.com'},
]

for i in range(1,10):
    temp = {'id':i,'username':'zhangsan'+str(i), 'age':'23', 'gender':'male', 'email':'289460'+str(i)+'@qq.com'}
    USER_LIST.append(temp)
def home(request):
    if request.method == "POST":
        username = request.POST.get('username')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        temp_1 = {'username':username, 'age':age, 'gender':gender}
        USER_LIST.append(temp_1)
    return render(request,'home.html' ,{'user_list':USER_LIST})


def son(request,id):
    #id = request.GET.get('id')

    if id:
        user_info = USER_LIST[int(id)]
    return render(request,'son.html', {'user_info':user_info})
