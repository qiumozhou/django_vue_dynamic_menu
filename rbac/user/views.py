from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from lib.utils import BaseResponse, initMenu
from user import models


def login(request):
    if request.method=="POST":
        username = request.POST.get("username")
        pwd = request.POST.get("password")
        user = models.User.objects.filter(user_name=username,password=pwd).first()
        if user:
            return BaseResponse(code="10000",msg="登陆成功",data={"user":user.user_name,"token":user.user_name})
        else:
            return BaseResponse(code="10004",msg="用户名或密码错误")


def userInfo(request):
    if request.method == "GET":
        userName = request.GET.get("token")
        user = models.User.objects.filter(user_name = userName).first()
        menu = [role.menu.all() for role in user.roles.all() ]
        menuData = initMenu(menu)
        userInfo={
            "avatar": 'https://wpimg.wallstcn.com/f778738c-e4f8-4870-b634-56703b4acafe.gif',
            "name": '邱墨舟',
            "menus":menuData
        }
        return BaseResponse(code="10000", msg="获取token成功",data=userInfo)


def logOut(request):
    if request.method == "POST":
        userInfo={
            "roles": ['admin'],
            "introduction": 'I am a super administrator',
            "avatar": 'https://wpimg.wallstcn.com/f778738c-e4f8-4870-b634-56703b4acafe.gif',
            "name": 'Super Admin'
        }
        return BaseResponse(code="10000", msg="退出登录",data=userInfo)