from django.contrib import admin
from queryKq.models import kaoqin
from django.http import StreamingHttpResponse
import xlwt

class kaoqinAdmin(admin.ModelAdmin):
    list_display = ('username', 'kq_sj')
    search_fields = ('username','kq_sj')
    list_filter = ('username','kq_sj')
    list_per_page = 30

admin.site.register(kaoqin,kaoqinAdmin)