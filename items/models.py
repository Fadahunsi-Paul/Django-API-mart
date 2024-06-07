from django.db import models

# Create your models here.
class Items(models.Model):
    item_id = models.PositiveIntegerField()
    name = models.CharField(max_length=100)
    price = models.DecimalField(decimal_places=2,max_digits=7)
    description = models.TextField()

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Items'
    