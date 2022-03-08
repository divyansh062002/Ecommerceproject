from django.db import models

# Create your models here.
class product(models.Model):
    p_id = models.SmallAutoField(primary_key=True)
    p_name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    size = models.CharField(max_length=10)
    p_descp = models.CharField(max_length=500, default='')
    image = models.ImageField(upload_to='products/')
    
    
    def get_all_products():
        return product.objects.all()