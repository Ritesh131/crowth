from django.contrib import admin
from django.utils.translation import ngettext
from .models import *

# Register your models here.
@admin.action(description='Duplicate Selected Record')
def make_published(modeladmin, request, queryset):
    print('dddd', queryset)
    for object in queryset:
        object.id = None
        object.save()



class BlogAdminView(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_active', 'created_date')
    list_display_links = ('id', 'title', 'created_date')
    list_editable = ('is_active',)
    actions = [make_published]


admin.site.register(Blog, BlogAdminView)