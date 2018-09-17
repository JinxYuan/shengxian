from django.shortcuts import render
from .models import TypeInfo, GoodsInfo
from django.core.paginator import *


def index(request):
    typeinfo = TypeInfo.objects.all()
    #  最新2个 推荐4个
    type0 = typeinfo[0].goodsinfo_set.order_by('-id')[0:2]
    type01 = typeinfo[0].goodsinfo_set.order_by('-gclick')[0:4]
    type1 = typeinfo[1].goodsinfo_set.order_by('-id')[0:2]
    type11 = typeinfo[1].goodsinfo_set.order_by('-gclick')[0:4]
    type2 = typeinfo[2].goodsinfo_set.order_by('-id')[0:2]
    type21 = typeinfo[2].goodsinfo_set.order_by('-gclick')[0:4]
    type3 = typeinfo[3].goodsinfo_set.order_by('-id')[0:2]
    type31 = typeinfo[3].goodsinfo_set.order_by('-gclick')[0:4]
    type4 = typeinfo[4].goodsinfo_set.order_by('-id')[0:2]
    type41 = typeinfo[4].goodsinfo_set.order_by('-gclick')[0:4]
    type5 = typeinfo[5].goodsinfo_set.order_by('-id')[0:2]
    type51 = typeinfo[5].goodsinfo_set.order_by('-gclick')[0:4]

    content = {'title': '首页',
               'page_name': 0,
               'guest_cart': 1,
               'type': typeinfo,
               'type0': type0, 'type01': type01,
               'type1': type1, 'type11': type11,
               'type2': type2, 'type21': type21,
               'type3': type3, 'type31': type31,
               'type4': type4, 'type41': type41,
               'type5': type5, 'type51': type51,
                }

    # return render(request, 'shengxianapp/print.html', content)

    return render(request, 'df_goods/index.html', content)


def list(request, tid, current_page, sort):
    typeinfo = TypeInfo.objects.get(pk=int(tid))
    new = typeinfo.goodsinfo_set.order_by('-id')[0:2]
    if sort == '1':
        # 默认
        goods_list = GoodsInfo.objects.filter(gtype_id=typeinfo.id).order_by('id')
    elif sort == '2':
        # 价格
        goods_list = GoodsInfo.objects.filter(gtype_id=typeinfo.id).order_by('gprice')
    elif sort == '3':
        # 人气
        goods_list = GoodsInfo.objects.filter(gtype_id=typeinfo.id).order_by('gclick')
    paginator = Paginator(goods_list, 2)
    page = paginator.page(int(current_page))
    content = {'title': typeinfo.ttitle,
               'page_name': 0,
               'guest_cart': 1,
               'new': new,
               'page': page,
               'typeinfo_id': typeinfo.id,
               'sort': sort,
               }
    return render(request, 'df_goods/list.html', content)


def detail(request, gid):
    goods = GoodsInfo.objects.get(pk=int(gid))
    goods.gclick = goods.gclick + 1
    goods.save()
    typeinfo = TypeInfo.objects.get(pk=goods.gtype_id)
    new = typeinfo.goodsinfo_set.order_by('-id')[0:2]
    content = {'page_name': 0,
               'guest_cart': 1,
               'new': new,
               'goods': goods}
    response = render(request, 'df_goods/detail.html', content)
    # 浏览记录
    goods_ids = request.COOKIES.get('goods_ids', '')
    goods_id = "%d"%goods.id
    if goods_ids != "": # 判断是否有历史纪录
        goods_ids1 = goods_ids.split(',') # 拆分为列表
        if goods_ids1.count(goods_id)>=1:
            goods_ids1.remove(goods_id)
        goods_ids1.insert(0, goods_id)
        if len(goods_ids1) >= 6:
            del goods_ids1[5]
        goods_ids = ','.join(goods_ids1)
    else:
        goods_ids = goods_id
    response.set_cookie('goods_ids', goods_ids)

    return response