from django.shortcuts import redirect
from django.http import HttpResponseRedirect, JsonResponse


# 定义一个装饰器
def checker(func):
    def checker_func(request, *args, **kwargs):
        # 判断用户是否登录，如果登录就直接执行函数；如果未登录就跳转到登录页面。

        if request.session.has_key('userId'):
            return func(request, *args, **kwargs)
        else:
            rdr = HttpResponseRedirect('/user/login')
            # 通过cookie记录访问地址，以便登录后跳转到访问的地址。
            rdr.set_cookie('url', request.get_full_path())
            return rdr
    return checker_func


def login_checker(func):
    def login_func(request, *args, **kwargs):
        # 判断用户是否登录，如果登录就直接执行函数；如果未登录就跳转到登录页面。

        if request.session.has_key('userId'):
            return func(request, *args, **kwargs)
        else:
            if request.is_ajax():
                return JsonResponse({'islogin': 0})
            else:
                return redirect('/user/login/')
    return login_func
