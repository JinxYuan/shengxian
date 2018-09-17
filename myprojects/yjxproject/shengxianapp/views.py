# coding=utf-8
from django.shortcuts import render, redirect
from .models import SXUser
from df_goods.models import GoodsInfo
from hashlib import sha1
from django.http import JsonResponse, HttpResponseRedirect
from . import user_decorator


def register(request):
    context = {'title': '用户注册'}
    return render(request, 'sx_user/register.html', context)


def register_exist(request):
    uname = request.GET.get('username')
    count = SXUser.objects.filter(username=uname).count()
    return JsonResponse({'count': count})


def register_handle(request):
    post = request.POST
    uname = post.get('user_name')
    upwd = post.get('pwd')
    upwd2 = post.get('cpwd')
    uemail = post.get('email')

    # 判断两次密码
    if upwd != upwd2:
        return redirect('/user/register')
    # 加密
    s1 = sha1()
    s1.update(upwd.encode('utf-8'))
    upwd3 = s1.hexdigest()

    # DB
    sxuser = SXUser()
    sxuser.username = uname
    sxuser.password = upwd3
    sxuser.uemail = uemail
    sxuser.save()
    return redirect('/user/login')


def login(request):
    uname = request.COOKIES.get('uname', '')
    context = {'title': '用户登录',
               'user_error': 0,
               'pwd_error': 0,
               'uname': uname}
    return render(request, 'sx_user/login.html', context)


def login_handle(request):
    post = request.POST
    uname = post.get('username')
    upwd = post.get('pwd')
    jizhu = post.get('jizhu', 0)

    # 加密
    s1 = sha1()
    s1.update(upwd.encode('utf-8'))
    upwd2 = s1.hexdigest()

    try:
        user = SXUser.objects.get(username=uname)
        # 登录成功
        if user.password == upwd2:
            url = request.COOKIES.get('url', '/goods')
            red = HttpResponseRedirect(url)
            # 记住用户名
            if jizhu != 0:
                red.set_cookie('uname', uname)
            else:
                red.set_cookie('uname', '', max_age=-1)
            request.session['user_id'] = user.id
            request.session['user_name'] = uname
            return red
        else:  # 密码错误
            context = {'title': '用户登录',
                       'user_error': 0,
                       'pwd_error': 1,
                       'uname': uname,
                       'upwd': upwd}
            return render(request, 'sx_user/login.html', context)
    except SXUser.DoesNotExist:
        # 用户名不存在
        context = {'title': '用户登录',
                   'user_error': 1,
                   'pwd_error': 0,
                   'uname': uname,
                   'upwd': upwd}
        return render(request, 'sx_user/login.html', context)


@user_decorator.login
def user_center_info(request):
    uemail = SXUser.objects.get(id=request.session['user_id']).uemail
    uname = request.session['user_name']
    # 最近浏览
    goods_ids = request.COOKIES.get('goods_ids', '')
    goods_ids1 = goods_ids.split(',')
    goods_list = []
    for goods_id in goods_ids1:
        if goods_id != '':
            goods_list.append(GoodsInfo.objects.get(id=int(goods_id)))

    context = {'title': '个人信息',
               'uemail': uemail,
               'uname': uname,
               'page_name': 1,
               'guest_cart': 0,
               'goods_list': goods_list}
    return render(request, 'sx_user/user_center_info.html', context)


@user_decorator.login
def user_center_order(request):
    context = {'title': '全部订单',
               'page_name': 1,
               'guest_cart': 0}
    return render(request, 'sx_user/user_center_order.html', context)


@user_decorator.login
def user_center_site(request):
    user = SXUser.objects.get(id=request.session['user_id'])
    if request.method == 'POST':
        post = request.POST
        user.ushouname = post.get('ushou')
        user.uaddress = post.get('uaddress')
        user.uyoubian = post.get('uyoubian')
        user.uphone = post.get('uphone')
        user.save()
    context = {'title': '收货地址',
               'user': user,
               'page_name': 1,
               'guest_cart': 0}
    return render(request, 'sx_user/user_center_site.html', context)


def logout(request):
    request.session.flush()
    return redirect('/goods')