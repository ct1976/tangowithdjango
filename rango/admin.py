from django.contrib import admin
from rango.models import Category,Page,UserProfile
from django.contrib.admin.templatetags.admin_modify import prepopulated_fields_js

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name'),}
    
admin.site.register(Category)
admin.site.register(Page)
admin.site.register(UserProfile)