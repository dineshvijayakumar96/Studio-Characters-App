from django.contrib import admin
from .models import Inquiry

# Customize the site header
admin.site.site_header = 'Studio Characters - Administration'

# Register your models here.
class InquiryAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'price', 'timestamp')
    search_fields = ('name', 'email', 'phone', 'timestamp')
    list_filter = ('email', 'phone', 'price', 'timestamp')

admin.site.register(Inquiry, InquiryAdmin)