from django.http import HttpRequest,HttpResponse
from django.middleware.csrf import CsrfViewMiddleware


# 定义一个URL类
class URL(object):
    def process_response(self, request, response):
        url_list = [
            '/user/register/',
            '/user/register_handle/',
            '/user/register_exist/',
            '/user/login/',
            '/user/login_handle/',
            '/user/logout/'
        ]
        if not request.is_ajax() and request.path not in url_list:
            response.set_cookie('url', request.get_full_path())
        return response