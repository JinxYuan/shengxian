from django.contrib import admin
from .models import TypeInfo, GoodsInfo


class TypeInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'ttitle']


class GoodsInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'gtitle', 'gprice', 'gunit', 'gclick', 'gkucun', 'gjianjie']


admin.site.register(TypeInfo, TypeInfoAdmin)
admin.site.register(GoodsInfo, GoodsInfoAdmin)
    # gcontent = HTMLField()
    # gpic = models.ImageField(upload_to='df_goods')
    # isDelete = models.BooleanField(default=False)
    # gtype = models.ForeignKey(TypeInfo)
