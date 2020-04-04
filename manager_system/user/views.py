from django.shortcuts import render,redirect
from user.models import Userinfo
# 加密模块
from hashlib import sha1

# Create your views here.
# 登录
def login(request):
    return render(request, 'user/login.html')
# 登录处理函数
def login_handle(request):
    # 获取表单的函数
    lname=request.POST.get('lname')
    lpwd=request.POST.get('lpwd')
    lcode=request.POST.get('code')

    # 根据lname查询是否有该账号
    users=Userinfo.objects.filter(username=lname)
    # 如果没有：重定向到登录页面
    if len(users)==0:
        return redirect('/user/login/')
    # 如果有：获取密码，进行判断
    else:
        upwd=users[0].password
        s1=sha1()
        s1.update(lpwd.encode('gbk'))
        # 提取cookie的验证码
        cookie_yzm=request.COOKIES.get('yzm')
        if s1.hexdigest()==upwd and lcode.lower()==cookie_yzm.lower():
            return redirect('/staff/home/')
        else:
            return redirect('/user/login/')
# 注册
def regist(request):
    return render(request, 'user/regist.html')
# 注册处理器
def regist_handle(request):
    # step1:获取表单数据
    uname=request.POST.get('uname')
    # 判断输入的账号是否存在:通过filter返回对象列表
    users=Userinfo.objects.filter(username=uname)
    if len(users)==0:
        upwd=request.POST.get('upwd')
        s1=sha1()
        s1.update(upwd.encode('gbk'))
        jm_pwd= s1.hexdigest()
        # step2:写入数据库
        user=Userinfo()
        user.username=uname
        user.password=jm_pwd
        user.save()
        # step3:重定向到登录页
        return redirect('/user/login/')
    else:
        return redirect('/user/regist/')

    # 验证码
from PIL import Image,ImageDraw,ImageFont
def vfcode(request):
    image=Image.new(
        'RGB',
        (100,40),
        (110,120,119)
    )
    font=ImageFont.truetype('arial.ttf',20)
    draw=ImageDraw.Draw(image)

    text="1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    import random
    cookie_yzm=""
    for x in range(4):
        ch=random.choice(text)
        cookie_yzm+=ch
        draw.text(
            (x*20+10,10),
            ch,
            (255,255,255),
            font,
        )

    import io
    bytes_io = io.BytesIO()
    image.save(bytes_io, 'png')

    from django.http import HttpResponse
    response = HttpResponse(bytes_io.getvalue(), 'image/png')
    response.set_cookie('yzm',cookie_yzm)
    return response