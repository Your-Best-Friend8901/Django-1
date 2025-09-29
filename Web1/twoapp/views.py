from django.shortcuts import render
from django.http import HttpResponse
from twoapp.function.main import check_password
from twoapp.function.web_register import data_user,login_data
from django.contrib import auth
# Create your views here.

def main(request):
    return render(request,'main/main.html')

def register(request):
    if request.method == "POST":
        nickname = request.POST.get("user_nickname")
        password = request.POST.get("user_password")
        result_func = check_password(nickname,password)
        if result_func == 'Пароль подходит!':
            result_data_base = data_user(nickname,password)
        context = {'text' : result_func,'text_database' : result_data_base}
        return render(request,'Enter/register/register.html',context)
    elif request.method == "GET":
        return render(request,'Enter/register/register.html')
    
def login(request):
    if request.method == 'GET':
        return render(request,'Enter/login/login.html')
    elif request.method =='POST':
        nickname = request.POST.get("user_nickname")
        password = request.POST.get("user_password")
        check_login = login_data(nick=nickname,password=password)
        context ={'result_login': check_login}
        return render(request,'Enter/login/login.html',context)
