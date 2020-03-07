from django.contrib import admin
from queryXiaofei.models import xiaofei
from django.http import StreamingHttpResponse
import xlwt

class xiaofeiAdmin(admin.ModelAdmin):
    list_display = ('username', 'wacc_sj','New_card_cash', 'New_card_subsidy', 'Cash_amt', 'Sub_amt')
    search_fields = ('username','wacc_sj')
    list_filter = ('username','wacc_sj')
    list_per_page = 30

admin.site.register(xiaofei,xiaofeiAdmin)