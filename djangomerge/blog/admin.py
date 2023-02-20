from django.contrib import admin
#from csvexport.actions import csvexport
import csv
from django.http import HttpResponse
from .models import *
from .forms import *

def download_csv(self, request, queryset):

    meta = self.model._meta
    field_names = [field.name for field in meta.fields]

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
    writer = csv.writer(response)

    writer.writerow(field_names)
    for obj in queryset:
       row = writer.writerow([getattr(obj, field) for field in field_names])

    return response

class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['name']

class PostAdmin(admin.ModelAdmin):
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "author":
            kwargs["queryset"] = Post.objects.filter()
        return super(PostAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == "tag":
            kwargs["queryset"] = Tag.objects.filter()
        return super(PostAdmin, self).formfield_for_manytomany(db_field, request, **kwargs)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "category":
            kwargs["queryset"] = Category.objects.filter()
        return super(PostAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)
    list_filter = ['category','tag','author','published_date']
    actions = [download_csv]
    list_display = ('title', 'author', 'published_date', 'thumbnail')
    search_fields = ['title']
    autocomplete_fields = ['category']
    readonly_fields=['thumbnail','featured']
    filter_horizontal = ('tag',)
    fieldsets = [
        ('Post Fields',{'fields':(('author',),('title',),('text',),)}),
        ('Media Fields',{'fields':(('featured_image','featured'),('thumbnail_image','thumbnail'),)}),
        ('Time Stamp',{'fields':(('created_date'),('published_date'),)}),
        ('Category Fields',{'fields':(('category',),('tag',),)}),]

class TagAdmin(admin.ModelAdmin):
    search_fields = ['name']

class CommentAdmin(admin.ModelAdmin):
    search_fields = ['comment']

admin.site.register(User)
admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Comment, CommentAdmin)

