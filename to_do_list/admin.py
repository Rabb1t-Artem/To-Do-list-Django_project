from django.contrib import admin
from to_do_list.models import Task, Tag


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("content", "create_date", "deadline", "completed")
    search_fields = ("content",)
    list_filter = ("completed",)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
