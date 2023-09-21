from django.contrib import admin

from . import models


class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "owner")


class LessonAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "video_url", "duration_seconds")


class AccessAdmin(admin.ModelAdmin):
    list_display = ("user", "product")


admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.Lesson, LessonAdmin)
admin.site.register(models.Access, AccessAdmin)
