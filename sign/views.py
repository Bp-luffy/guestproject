from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from django.contrib import auth
from sign.models import Event,Guest

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
    event_list=Event.objects.all()
    #username=request.COOKIES.get('user','') #读取浏览器cookie
    username=request.session.get('user','') #读取浏览器session
    return render(request,'event_manage.html',{'user':username,'events':event_list})

#发布会名称搜索
@login_required
def search_name(request):
    username=request.session.get('user','')
    search_name=request.GET.get('name','')
    event_list=Event.objects.filter(name__icontains=search_name)
    return render(request,"event_manage.html",{'user':username,'events':event_list})

#嘉宾管理
@login_required
def guest_manage(request):
    username=request.session.get('user','')
    guest_list=Guest.objects.all()
    return render(request,"guest_manage.html",{"user":username,"guests":guest_list})