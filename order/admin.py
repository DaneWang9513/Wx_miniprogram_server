from django.contrib import admin
from order.models import Order,TodayOrder
from django.http import StreamingHttpResponse
import xlwt
# Register your models here.

admin.site.site_title="管理后台"
admin.site.site_header="管理后台"
admin.site.index_title="功能项"


class orderAdmin(admin.ModelAdmin):
    list_display = ('food_name','number','typeName','username','first_name','dept','state','date_time','lq_date_time')
    search_fields = ('food_name','number','typeName','state','first_name')
    list_filter = ('date_time','username','food_name','number','typeName','state')
    list_per_page = 1500
    actions = ["export_excel"]
    date_hierarchy = 'lq_date_time'
    def export_excel(self,request,queryset):
        Begin = xlwt.Workbook()
        sheet = Begin.add_sheet("order")
        rows = 0
        col_header = ['名字','数量','星期','工号','姓名','部门','下单时间']
        font_style = xlwt.XFStyle()
        font_style.font.bold = True
        for col in range(len(col_header)):
            sheet.write(rows,col,col_header[col],font_style)
        for query in queryset:
            # you need write colms
            # 好像有个方法可以一次性写入所有列，记不清了，只能用这种简单的方法去实现
            rows += 1
            sheet.write(rows, 0, str(query.food_name))
            sheet.write(rows, 1, str(query.number))
            sheet.write(rows, 2, str(query.typeName))
            sheet.write(rows, 3, str(query.username))
            sheet.write(rows, 4, str(query.first_name))
            sheet.write(rows, 5, str(query.dept))
            sheet.write(rows, 6, str(query.date_time))
        Begin.save("%s" % ('order.xls'))

        def file_iterator(filename, chuck_size=512):
            with open(filename, "rb") as f:
                while True:
                    c = f.read(chuck_size)
                    if c:
                        yield c
                    else:
                        break

        response = StreamingHttpResponse(file_iterator('order.xls'))
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = 'attachment;filename="{}"'.format("order.xls")
        return response

    export_excel.short_description = "导出Excel"  # 按钮显示名字


class TodayOrderAdmin(admin.ModelAdmin):
    list_display = ('food_name','number')
    list_filter = ('date_time','food_name')
    date_hierarchy = 'date_time'
    list_per_page = 30

admin.site.register(Order, orderAdmin)
admin.site.register(TodayOrder, TodayOrderAdmin)
