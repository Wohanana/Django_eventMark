from django.shortcuts import render,redirect
from . import models
from .forms import UserForm,RegisterForm
from mark.models import Marktxt
from django.http import HttpResponse
import json


def login(request):
    if request.session.get('is_login',None):
        return redirect('/index/')
 
    if request.method == "POST":
        login_form = UserForm(request.POST)
        message = "请检查填写的内容！"
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            try:
                user = models.User.objects.get(username=username)
                if user.password == password:
                    request.session['is_login'] = True
                    request.session['is_superuser'] = user.is_superuser
                    request.session['user_name'] = user.username
                    request.session['is_headman'] = user.is_headman
                    request.session['is_group']=user.is_group
                    request.session['group']=user.group
                    return redirect("/mark/txtlist")
                else:
                    message = "密码不正确！"
            except:
                message = "用户不存在！"
        return render(request, 'login.html', locals())
 
    login_form = UserForm()
    return render(request, 'login.html', locals())

def register(request):
    if request.session.get('is_login', None):
        # 登录状态不允许注册。你可以修改这条原则！
        return redirect("/index/")
    if request.method == "POST":
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():  # 获取数据
            username = register_form.cleaned_data['username']
            password1 = register_form.cleaned_data['password1']
            password2 = register_form.cleaned_data['password2']
            if password1 != password2:  # 判断两次密码是否相同
                message = "两次输入的密码不同！"
                return render(request, 'register.html', locals())
            else:
                same_name_user = models.User.objects.filter(username=username)
                if same_name_user:  # 用户名唯一
                    message = '用户已经存在，请重新选择用户名！'
                    return render(request, 'register.html', locals())
                # 当一切都OK的情况下，创建新用户 
                new_user = models.User.objects.create()
                new_user.username = username
                new_user.password = password1
                new_user.is_headman = False
                new_user.save()
                message = "注册成功！"
    register_form = RegisterForm()
    return render(request, 'register.html', locals())

def logout(request):
    if not request.session.get('is_login', None):
        # 如果本来就未登录，也就没有登出一说
        return redirect("/index/")
    request.session.flush()
    # 或者使用下面的方法
    # del request.session['is_login']
    # del request.session['user_id']
    # del request.session['user_name']
    return redirect("/index/")


def join(request):
    json_receive = json.loads(request.body)
    username=json_receive['username']
    user = models.User.objects.get(username=username)
    user.group=json_receive['group']
    user.is_group=True
    user.save()
    request.session['is_group']=True
    request.session['group']=user.group
    return render(request,'list.html')

def head(request):
    json_receive = json.loads(request.body)
    same_new_head = models.Headman.objects.filter(username=json_receive['username'])
    if same_new_head:
        pass
    else:
        new_head = models.Headman.objects.create()
        new_head.username =json_receive['username']
        new_head.is_headman =json_receive['bool']
        new_head.group=json_receive['group']
        new_head.save()
    return HttpResponse("success")
    
def head_confirm(request):
    json_receive = json.loads(request.body)
    user = models.User.objects.get(username=json_receive['username'])
    user.is_headman=True
    user.save()
    models.Headman.objects.get(username=json_receive['username']).delete()
    return HttpResponse("success")
    


