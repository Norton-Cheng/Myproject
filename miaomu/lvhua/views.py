from django.shortcuts import render,redirect
from lvhua.models import Message

# Create your views here.

# 网站首页
def index(request):

    return render(request,'lvhua/index.html')

# 关于我们
def about(request):

    return render(request,'lvhua/about.html')

# 在线留言
def message(request):

    return render(request,'lvhua/message.html')

# 在线留言处理
def messagehandle(request):
    # 获取form表单数据
    name = request.POST.get('name')
    phone = request.POST.get('tel')
    email = request.POST.get('email')
    address = request.POST.get('adr')
    beizhu=request.POST.get('content')

    # 将数据写入数据库
    user = Message()
    user.pname = name
    user.pphone = phone
    user.pemail = email
    user.padderss = address
    user.pbeizhu=beizhu
    user.save()
    return render(request,'lvhua/index.html')

# 产品中心
def product(request):

    return render(request,'lvhua/product.html')

# 产品展示
def productshow(request):

    return render(request,'lvhua/productshow.html')

# 产品分类
def productcate(request):

    return render(request,'lvhua/productcate.html')

# 基地展示
def jidi(request):

    return render(request,'lvhua/jidi.html')

# 资质荣誉
def honor(request):

    return render(request,'lvhua/honor.html')

# 新闻中心
def news(request):

    return render(request,'lvhua/news.html')

# 信息展示
def newsshow(request):

    return render(request,'lvhua/newsshow.html')

# 联系我们
def contact(request):

    return render(request,'lvhua/contact.html')