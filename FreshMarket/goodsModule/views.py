from django.shortcuts import render
from goodsModule import views


# Create your views here.
def index(request):
    context = {'title': '首页'}
    return render(request, 'goodsModule/index.html', context)
