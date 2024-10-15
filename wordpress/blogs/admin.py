from django.contrib import admin
from .models import Author,Post,Tag
# Register your models here.
class PostAdmin(admin.ModelAdmin):

    list_filter = ("date","tags","author",)
    list_display = ("title","date","author",)
    prepopulated_fields = {"slug" : ("title",)}

admin.site.register(Author)
admin.site.register(model_or_iterable=Post,admin_class=PostAdmin)
admin.site.register(Tag)
