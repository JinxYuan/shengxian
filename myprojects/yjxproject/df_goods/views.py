from django.shortcuts import render
from .models import TypeInfo,GoodsInfo
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
               'typeinfo_id': typeinfo.id
               }
    return render(request, 'df_goods/list.html', content)


def detail(request, gid):
    goods = GoodsInfo.objects.get(pk=int(gid))
    typeinfo = TypeInfo.objects.get(pk=goods.gtype_id)
    new = typeinfo.goodsinfo_set.order_by('-id')[0:2]
    content = {'page_name': 0,
               'guest_cart': 1,
               'new': new,
               'goods': goods}
    return  render(request, 'df_goods/detail.html', content)