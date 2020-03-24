from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from django.contrib import auth

# Create your views here.
def index(request):
    return render(request,'index.html')


#登录动作
def login_action(request):
    if request.method=='POST':
        username=request.POST.get('username','')
        password=request.POST.get('password','')
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            request.session['user']=username #将session信息记录到浏览器
            response=HttpResponseRedirect('/sign/event_manage/')
            #response.set_cookie('user',username,3600) #添加浏览器cookie
            return response
        else:
            return render(request,'index.html',{'error':'username or password error!'})

#发布会管理
@login_required
def event_manage(request):
    #username=request.COOKIES.get('user','') #读取浏览器cookie
    username=request.session.get('user','') #读取浏览器session
    return render(request,'event_manage.html',{'user':username})
