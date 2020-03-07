from django.contrib import admin
from order_tj.models import Order_tj
from django.http import StreamingHttpResponse
import xlwt
# Register your models here.

class order_tjAdmin(admin.ModelAdmin):
    list_display = ('lq_date_time','dept','number_h1','number_h2')
    search_fields = ('lq_date_time','dept')
    list_filter = ('lq_date_time','dept')
    list_per_page = 100
    actions = ["export_excel"]
    date_hierarchy = 'lq_date_time'
    def export_excel(self,request,queryset):
        Begin = xlwt.Workbook()
        sheet = Begin.add_sheet("order")
        rows = 0
        col_header = ['领取时间','部门','盒饭1数量','盒饭2数量']
        font_style = xlwt.XFStyle()
        font_style.font.bold = True
        for col in range(len(col_header)):
            sheet.write(rows,col,col_header[col],font_style)
        for query in queryset:
            # you need write colms
            # 好像有个方法可以一次性写入所有列，记不清了，只能用这种简单的方法去实现
            rows += 1
            sheet.write(rows, 0, str(query.lq_date_time))
            sheet.write(rows, 1, str(query.dept))
            sheet.write(rows, 2, str(query.number_h1))
            sheet.write(rows, 3, str(query.number_h2))
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


admin.site.register(Order_tj, order_tjAdmin)