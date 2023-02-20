from django.contrib import admin
from .models import Product ,Test

# Register your models here.

admin.site.register(Product)
admin.site.site_header = 'Mohammed'
admin.site.site_title = 'Mohammed'

