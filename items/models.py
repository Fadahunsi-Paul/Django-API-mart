from django.db import models

# Create your models here.
class Items(models.Model):
    category_name = models.ForeignKey('Item_category',related_name='Item_Types',on_delete=models.CASCADE)
    item_id = models.PositiveIntegerField()
    name = models.CharField(max_length=100)
    price = models.DecimalField(decimal_places=2,max_digits=7)
    description = models.TextField()

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Items'


class Item_category(models.Model):
    category_id = models.PositiveIntegerField()
    category_name = models.CharField(max_length=100,)
    
    def __str__(self):
        return self.category_name
    

    class Meta:
        verbose_name_plural = 'Item_category'

    