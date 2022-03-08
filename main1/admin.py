from django.contrib import admin
from main1.models import product
# Register your models here.


class Adminproducts(admin.ModelAdmin):
    list_display = ['p_id','p_name','price','image','size','p_descp']

admin.site.register(product,Adminproducts)