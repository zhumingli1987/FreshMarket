from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, JsonResponse
from django.db.models import Max
from userModule.models import *
from hashlib import sha1


# Create your views here.
def index(request):
    return render(request, 'userModule/index.html')


def register(request):
    context = {'title': '用户注册'}
    return render(request, 'userModule/register.html', context)


def register_exist(request):
    name = request.GET.get('userName')
    count = UserInfo.users.filter(userName=name).count()
    return JsonResponse({'count': count})


def register_handle(request):
    # 接收表单提交数据
    post = request.POST
    user_name = post.get('user_name')
    fpwd = post.get('pwd')
    spwd = post.get('cpwd')
    email = post.get('email')

    # 判断两次输入的密码是否一致
    if fpwd != spwd:
        return redirect('/user/register')

    # 密码加密
    s1 = sha1()
    s1.update(fpwd.encode())
    pwd = s1.hexdigest()

    # 生成自定义userId
    result = UserInfo.users.aggregate(Max('userID'))
    num = result['userID__max']
    if num is not None and num > 100000:
        userId = num + 1
    else:
        userId = 100001

    # 创建对象
    user = UserInfo.users.create(userId, user_name, pwd, email)
    user.save()

    # 注册成功，返回登录页面
    return render(request, 'userModule/login.html')


def login(request):
    context = {'title': '用户登录'}
    return render(request, 'userModule/login.html', context)


def login_handle(request):
    # 接收请求数据
    post = request.POST
    name = post.get('userName')
    pwd = post.get('pwd')
    rmb = post.get('rmb', 0)
    # 根据用户名查询对象
    user = UserInfo.users.filter(userName=name)
    print(user)
    # 判断用户是否存在，如果不存在直接返回；如果存在再判断输入密码是否正确。
    if len(user) == 1:
        s = sha1()
        s.update(pwd.encode())
        if s.hexdigest() == user[0].password:
            url = request.COOKIES.get('url', '/')
            rdr = HttpResponseRedirect(url)
            # 登录成功后，删除转向地址，防止以后直接登录造成的转向
            rdr.set_cookie('url', '', max_age=-1)
            # 记住用户名
            if rmb != 0:
                rdr.set_cookie('userName', name)
            else:
                rdr.set_cookie('userName', '', max_age=-1)
            request.session['userId'] = user[0].userID
            request.session['userName'] = name
            return rdr
        else:
            context = {'title': '用户登录', 'error_name': 0, 'userName': name, 'error_pwd': 1, 'userId': pwd}
            return render(request, 'userModule/login.html', context)
    else:
        context = {'title': '用户登录', 'error_name': 1, 'userName': name, 'error_pwd': 0, 'userId': pwd}
        return render(request, 'userModule/login.html', context)





