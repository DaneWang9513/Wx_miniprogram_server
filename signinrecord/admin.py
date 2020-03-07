from django.contrib import admin
from signinrecord.models import SigninRecord
from django.http import StreamingHttpResponse
import xlwt
# Register your models here.
class signinrecordAdmin(admin.ModelAdmin):
    list_display = ('studentID', 'studentName', 'topic')
    search_fields = ('topic','studentName')
    list_filter = ('studentID', 'studentName', 'topic')
    list_per_page = 30

admin.site.register(SigninRecord, signinrecordAdmin)