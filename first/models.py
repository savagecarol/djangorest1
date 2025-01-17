from django.db import models

# Create your models here.
class Products(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=20)
    description = models.TextField(default='',blank=True)
    price =models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self):
        return self.name


