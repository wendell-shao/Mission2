from django.contrib import admin
from .models import Category
from .models import Activity, Article
from .models import Slogan

# Register your models here.

admin.site.site_header = '后台管理'
admin.site.site_title = '后台管理'


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'create_time', 'status', ]
    search_fields = ['name', 'create_time', ]

    actions = None

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ['title', 'submitter', 'create_time',
                    'update_time', 'publish_date', 'status']
    search_fields = ['title', 'content', 'publish_date',
                     'image', 'status']
    actions = None

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset

    class Media:
         css = {
             'all': (
                 'css/simditor.css',
                 'css/textarea.css'
             )
         }


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'submitter', 'create_time',
                    'update_time', 'publish_date', 'image', 'status']
    search_fields = ['title', 'content', 'publish_date',
                     'image', 'status']
    actions = None

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset

    class Media:
         css = {
             'all': (
                 'css/simditor.css',
                 'css/textarea.css'
             )
         }
    #     js = (
    #         'https://cdn.bootcss.com/jquery/3.2.1/jquery.js',
    #         'js/simditor/module.js',
    #         'js/simditor/uploader.js',
    #         'js/simditor/hotkeys.js',
    #         'js/simditor/simditor.js',
    #         'js/textarea.js',
    #     )


@admin.register(Slogan)
class SloganAdmin(admin.ModelAdmin):

    list_display = ['title', ]
    search_fields = ['title', ]
    actions = None

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset

    class Media:
         css = {
             'all': (
                 'css/simditor.css',
                 'css/textarea.css'
             )
         }


admin.site.register(Category, CategoryAdmin)