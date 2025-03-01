from django.contrib import admin
from api.models import Post, Category

class BaseAdmin(admin.ModelAdmin):
    list_per_page = 10

    class Meta:
        abstract = True


class PostAdmin(BaseAdmin):
    list_display = [f.name for f in Post._meta.fields]


class CategoryAdmin(BaseAdmin):
    list_display = [f.name for f in Category._meta.fields]

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)