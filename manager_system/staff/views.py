from django.shortcuts import render,redirect
from staff.models import Staffinfo
from django.core.paginator import *

# Create your views here.
def home(request):
    # 获取数据库的所有数据
    all_staffs=Staffinfo.objects.all()
    # 创建分页对象
    pn=Paginator(all_staffs,2)
    # 创建页面对象
    index=request.GET.get('page',1)
    pg=pn.page(int(index))
    # 定义字典传递-context
    context={
        'all_staffs':all_staffs,
        'pg_staffs':pg,
        'pn':pn,
    }
    return render(request,'staff/home.html',context)

# 详情页
def detail(request,sid):
    staffs= Staffinfo.objects.filter(id=int(sid))
    if len(staffs)!=0:
        staff=staffs[0]
    else:
        staff='未找到'
    context={
        'staff':staff
    }
    return render(request,'staff/detail.html',context)

# 删除
def delete(request,sid):
# 根据id删除对应的数据
    Staffinfo.objects.filter(id=int(sid)).delete()
# 重定向到首页
    return redirect('/staff/home/')

# 添加
def add(request):
    context={
        'title':'添加',
    }
    return render(request,'staff/add.html',context)

# 添加-处理函数
def add_handle(request):
    # 重定向到home
    staff=Staffinfo()
    save_staff(request,staff)
    return redirect('/staff/home/')

# 编辑
def edt(request):
    sid=request.GET.get('id')
    context = {
        'title': '编辑',
        'sid':sid,
        'staff':Staffinfo.objects.get(id=sid)
    }
    return render(request, 'staff/edt.html', context)

# 编辑-处理函数
def edt_handle(request):
    sid = request.GET.get('id')
    staff=Staffinfo.objects.get(id=sid)
    save_staff(request, staff)
    return redirect('/staff/home/')

def save_staff(request,staff):
    # 获取form表单数据
    name = request.POST.get('name')
    birthday = request.POST.get('birthday')
    gender = request.POST.get('gender')
    phone = request.POST.get('phone')
    salary = request.POST.get('salary')
    dep = request.POST.get('dep')
    # 给对象赋值
    staff.name = name
    staff.birthday = birthday
    staff.gender = gender
    staff.phone = phone
    staff.salary = salary
    staff.department = dep
    staff.save()