from django.contrib import admin
from django.utils.translation import ngettext
from .models import *

# Register your models here.
@admin.action(description='Duplicate Selected Record')
def make_published(modeladmin, request, queryset):
    for object in queryset:
        object.id = None
        object.save()



class BlogAdminView(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_active', 'created_date')
    list_display_links = ('id', 'title', 'created_date')
    list_editable = ('is_active',)
    actions = [make_published]


class QueryAdminView(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone', 'created_date')
    search_fields = ('name', 'email', 'phone')


admin.site.register(Blog, BlogAdminView)
admin.site.register(Query, QueryAdminView)
admin.site.register(Services)