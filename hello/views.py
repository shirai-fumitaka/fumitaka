from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from .form import CheckForm,HelloForm,FriendForm,FindForm,MessageForm
from .models import Friend
from django.shortcuts import redirect
from django.views.generic import ListView
from django.views.generic import DetailView
from django.db.models import Q
from django.db.models import Count,Sum,Avg,Min,Max
from django.core.paginator import Paginator
from .models import Friend,Message

def index(request,num=1):
    data = Friend.objects.all()
    page = Paginator(data,3)

    params = {
        'title':'Hello',
        'data':page.get_page(num),
    }
    return render(request,'hello/index.html',params)

def create(request):
    params ={
        'title':'Hello',
        'form':FriendForm(),
    }
    if  request.method == 'POST':
        obj = Friend()
        friend = FriendForm(request.POST,instance=obj)
        friend.save()
        return redirect(to='/hello/')
    return render(request,'hello/create.html',params)

def edit(request,num):
    obj = Friend.objects.get(id=num)
    if (request.method == 'POST'):
        friend = FriendForm(request.POST,instance=obj)
        friend.save()
        return redirect(to='/hello/friend/')
    params = {
        'title':'Hello',
        'id':num,
        'form':FriendForm(instance=obj),
    }
    return render(request,'hello/edit.html',params)

def delete(request,num):
    obj = Friend.objects.get(id=num)
    if(request.method == 'POST'):
        obj.delete()
        return redirect(to='/hello/friend/')
    params = {
        'title':'Hello',
        'id':num,
        'obj':obj,
    }
    return render(request,'hello/delete.html',params)

class FriendList(ListView):
    model = Friend

class FriendDetail(DetailView):
    model = Friend

def find(request):
    if (request.method == 'POST'):
        form = FindForm(request.POST)
        find = request.POST['find']
        list = find.split()
        data = Friend.objects.all()[int(list[0]):int(list[1])]
    else:
        form = FindForm()
        data = Friend.objects.all()
    params = {
        'title':'Hello',
        'form':form,
        'data':data,
    }
    return render(request,'hello/find.html',params)

def check(request):
    params = { 
        'title':'Hello',
        'message':'check validation',
        'form':FriendForm()
    }
    if(request.method == 'POST'):
        obj = Friend()
        form = FriendForm(request.POST,instance=obj)
        params['form'] = form
        if form.is_valid():
            params['message'] = 'OK!'
        else:
            params['message'] = 'no good.'
    return render(request,'hello/check.html',params)

def message(request,page=1):
    if(request.method=='POST'):
        obj = Message()
        form = MessageForm(request.POST,instance=obj)
        form.save()
    data = Message.objects.all().reverse()
    paginator = Paginator(data,3)
    params = {
        'title':'Hello',
        'form':MessageForm(),
        'data':paginator.get_page(page),
    }
    return render(request,'hello/message.html',params)


    #     name = request.POST('name')
    #     mail = request.POST('mail')
    #     age = int(request.POST('age'))  # デフォルト値として0を設定
    #     birthday = request.POST('birthday')
    #     if name and mail and age and birthday:  # 全てのフィールドが存在することを確認
    #         friend = Friend(name=name,mail=mail,age=age,birthday=birthday)
    #         friend.save()
    #         return redirect(to='/hello/friend/')
    # return render(request,'hello/create.html',params)

    # if (request.method == 'POST'):
    #     num = request.POST['id']
    #     item = Friend.objects.get(id=num)
    #     params['data'] = [item]
    #     params['form'] = HelloForm(request.POST)
    # else:
    #     params['data'] = Friend.objects.all()
    # return render(request,'hello/index.html',params)
class HelloView(TemplateView):
    def __init__(self):
        self.params = {
            'title':'Hello',
            # 'message':'your data:',
            'form':CheckForm(),
            'result':None,
        }
    def get(self,request):
        return render(request,'hello/index.html',self.params)
    def post(self,request):
        ch = request.POST.getlist('choice')
        self.params = {
            'title':'Hello',
            'form':CheckForm(request.POST),
            'result':'あなたは、' + str(ch) + 'を選びました。',                
            }
        return render(request,'hello/index.html',self.params)
    
        # chk = request.POST.get('check')
        # self.params = { 
        #     'title':'Hello',
        #     'form':checkForms(request.POST),
        #     'result':chk,
        # }
        # return render(request,'hello/index.html',self.params)
    
        # if 'check' in request.POST:
        #     self.params['result'] = 'Check it out!'
        # else:
        #     self.params['result'] = 'You checked it.'
        # self.params['form'] = CheckForm(request.POST)
        # return render(request,'hello/index.html',self.params)

        # msg = 'あなたは、<b>' + request.POST['name'] + \
        # '(' + request.POST['age']+\
        # request.POST['mail'] + ')です。<br>'
        # title = request.POST['name']
        # self.params['title'] = title
        # self.params['message'] = msg
        # self.params['form'] = HelloForm(request.POST)
        # return render(request,'hello/index.html',self.params)

# def index(request):
#     params = {
#         'title':'Hello/Index',
#         'msg':'This is sample page.',
#         'goto':'next',
#         'form':HelloForm(),
#     }
#     if (request.method == 'POST'):
#         params['message'] = '名前：' + request.POST['name'] + \
#             '<br>メール：' + request.POST['mail'] + \
#             '<br>年齢:'+ request.POST['age']
#         params['form'] = HelloForm(request.POST)
#     return render(request, 'hello/index.html',params)
#  Create your views here.

# def next(request):
#     params = {
#         'title':'Hello/Next',
#         'msg':'This is next page.',
#         'goto':'index',
#     }
#     return render(request, 'hello/index.html',params)

# def form(request):
#     msg = request.POST['msg']
#     params = {
#         'title':'Hello/Form',
#         'msg':msg,
#         'goto':'index',
#     }
#     return render(request, 'hello/index.html',params)
