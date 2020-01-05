from django.shortcuts import render
from apitest.models import Apitest, Apistep

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import  login_required
from django.contrib import auth
from django.contrib.auth import authenticate, login

# create your views here.

def test(request):
    #request参数：用于生成此响应的请求对象
    return HttpResponse("Hello test") # 返回Httpreponse响应函数

def login_simple_test(request):
    return render(request, 'login.html')

def login(request):
    if request.POST:
#在登录页面输入用户名密码,点击登录，
#form表单把输入的信息,浏览器信息,客户端地址,访问地址等封装到request对象里,
#以post的形式发送给login的url
        username = password = ''
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            auth.login(request, user)
            request.session['user'] = username
            response = HttpResponseRedirect('/home/')
            return response
        else:
            return render(request,'login.html',{'error':'username or password error'})
#    else:
#        contxet = {}
#        return render(request,'login.html',contxet)

    return render(request, 'login.html')

def home(request):
    return render(request, 'home.html')

def logout(request):
    auth.logout(request)
    return render(request,'login.html')

#接口管理
@login_required #其作用就是告诉程序，使用这个方法是要求用户登录的
def apitest_manage(request):
    apitest_list = Apitest.objects.all() #读取所有流程接口数据
    username = request.session.get('user', '') #读取浏览器登陆Session
    return render(request, 'apitest_manage.html', {'user':username, 'apitests':apitest_list})#定义流程接口数据的变量并返回到前端

#接口步骤管理
@login_required
def apistep_manage(request):
    username = request.session.get('user', '')
    apistep_list = Apistep.objects.all()
    return render(request, 'apistep_manage.html', {'user':username, 'apisteps':apistep_list})