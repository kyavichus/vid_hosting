from django.contrib import admin
from .models import Video, Rating, Category



class CategoryAdmin(admin.ModelAdmin):
    list_display = ('cat_name', 'slug',)
    prepopulated_fields = {'slug': ('cat_name',)}

admin.site.register(Video)
admin.site.register(Rating)
admin.site.register(Category, CategoryAdmin)
