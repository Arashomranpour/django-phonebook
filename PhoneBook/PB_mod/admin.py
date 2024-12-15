from django.contrib import admin

# Register your models here.
from .models import Contact
class ContactAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Contact._meta.get_fields()]
    
    
admin.site.register(Contact,ContactAdmin)
