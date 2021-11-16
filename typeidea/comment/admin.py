from django.contrib import admin
from .models import Comment
from typeidea.base_admin import BaseOwnerAdmin
# Register your models here.


@admin.register(Comment)
# BaseOwnerAdmin不适用，comment没有owner属性
# BaseOwnerAdmin被blog的models继承了，而没有被comment的models继承
class CommentAdmin(admin.ModelAdmin):
    list_display = ('target', 'nickname', 'content', 'website', 'created_time')
