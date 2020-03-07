from django.contrib import admin
from queryMenu.models import menu
# Register your models here.

class menuAdmin(admin.ModelAdmin):
    list_display = ('typeName','name','sales','sales_fz','lq_date_time','image_data','status','xiaoliang','fh_status')
    list_editable = ['status']
    readonly_fields = ('image_data',)  # 必须加这行 否则访问编辑页面会报错
    search_fields = ('typeName','name')
    list_filter = ('typeName','status','name','lq_date_time')
    date_hierarchy = 'lq_date_time'
    list_per_page = 10

admin.site.register(menu,menuAdmin)