from django.db import models

class Category(models.Model):
    name=models.CharField(max_length=50)
    def __str__(self):
        return self.name
    
    
class Book(models.Model):
    
    status_book=[('availble','availble'),
                 ('rental','rental'),
                 ('solid','solid'),]
    
    title= models.CharField(max_length=250)
    author= models.CharField(max_length=250,null=True, blank=True)
    photo_book=models.ImageField(upload_to='photos',null=True, blank=True) # upload_to='photos' يجب تحميل هذا في التيرمينال "pip install pillow"سبب استخدام 
    photo_author=models.ImageField(upload_to='photos',null=True, blank=True)
    pages=models.IntegerField(null=True, blank=True)
    price=models.DecimalField(max_digits=5,decimal_places=2,null=True, blank=True)#"null=True, blank=True لانو ممكن يكون للايجار مش البيع "
    rental_price_day=models.DecimalField(max_digits=5,decimal_places=2,null=True, blank=True)
    rental_period=models.IntegerField(null=True, blank=True)
    total_rental=models.DecimalField(max_digits=5,decimal_places=2,null=True, blank=True)#"null=True, blank=True لانو ممكن يكون للايجار مش البيع "
    active=models.BooleanField(default=True)
    status=models.CharField(max_length=50,choices=status_book,null=True, blank=True)
    category=models.ForeignKey(Category,on_delete=models.PROTECT,null=True, blank=True)
    
    def __str__(self):
        return self.title