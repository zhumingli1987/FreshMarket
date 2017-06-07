from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from django.db.models import Max
from userModule.models import *
from hashlib import sha1
from userModule.decorator_login import checker


# Create your views here.
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
    rmb = int(post.get('rmb', 0))
    print(type(rmb))
    # 根据用户名查询对象
    user = UserInfo.users.filter(userName=name)
    # 判断用户是否存在，如果不存在直接返回报错；如果存在再判断输入密码是否正确。
    if len(user) != 0:
        s = sha1()
        s.update(pwd.encode())
        print(s.hexdigest())
        print(user[0].password)
        # 判断用户密码是否正确，如果正确登录成功，不正确就返回报错。
        if s.hexdigest() == user[0].password:
            # 获取用户登录后需要跳转的页面。
            url = request.COOKIES.get('url', '/')
            # 跳转到指定页面或者首页。
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
            context = {'title': '用户登录', 'error_name': 0, 'userName': name, 'error_pwd': 1, 'pwd': pwd}
            return render(request, 'userModule/login.html', context)
    else:
        context = {'title': '用户登录', 'error_name': 1, 'userName': name, 'error_pwd': 0, 'pwd': pwd}
        return render(request, 'userModule/login.html', context)


def logout(request):
    request.session.flush()
    return redirect('/')


@checker
def user_center(request):
    user = UserInfo.users.get(userID=request.session['userId'])
    if Address.adds.filter(addToUser=user).exists():
        add = Address.adds.get(addToUser=user)
        context = {'title': '用户中心', 'page_name': 1, 'user': user, 'add': add}
    else:
        context = {'title': '用户中心', 'page_name': 1}
    #  需要插入最近浏览的商品。
    return render(request, 'userModule/user_center_info.html', context)


@checker
def user_order(request):
    context = {'title': '用户中心', 'page_name': 1}
    return render(request, 'userModule/user_center_order.html', context)


@checker
def user_site(request):
    user = UserInfo.users.get(userID=request.session['userId'])
    if request.method == 'POST':
        if Address.adds.filter(addToUser=user).exists():
            add = Address.adds.get(addToUser=user)
            post = request.POST
            add.receiveName = post.get('receiveName')
            add.addressInfo = post.get('addressInfo')
            add.mailId = post.get('mailId')
            add.receiveTel = post.get('receiveTel')
            add.save()
        else:
            # 生成自定义userId
            result = Address.adds.aggregate(Max('addressId'))
            num = result['addressId__max']
            print(num)
            if num is not None and num > 100000:
                addId = num + 1
            else:
                addId = 100001
            post = request.POST
            name = post.get('receiveName')
            address = post.get('addressInfo')
            mail = post.get('mailId')
            telephone = post.get('receiveTel')
            user = UserInfo.users.get(userID=request.session['userId'])
            add = Address.adds.create(addId, address, name, mail, telephone, user)
            add.save()
        context = {'title': '用户中心', 'page_name': 1, 'add': add}
    else:
        if Address.adds.filter(addToUser=user).exists():
            add = Address.adds.get(addToUser=user)
            context = {'title': '用户中心', 'page_name': 1, 'add': add}
        else:
            context = {'title': '用户中心', 'page_name': 1}
    return render(request, 'userModule/user_center_site.html', context)
