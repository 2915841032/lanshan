from django.contrib import admin
from .models import Subject, Teacher


# 学科管理类，定制后台显示的字段和排序方式
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('no', 'name', 'create_date', 'is_hot')  # 在列表页显示的字段
    ordering = ('no',)  # 排序字段


# 老师管理类，定制后台显示的字段和排序方式
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('no', 'name', 'detail', 'good_count', 'bad_count', 'subject')  # 列表页显示字段
    ordering = ('subject', 'no')  # 排序字段


# 注册Subject模型和对应的管理类到Django后台
admin.site.register(Subject, SubjectAdmin)
# 注册Teacher模型和对应的管理类到Django后台
admin.site.register(Teacher, TeacherAdmin)
