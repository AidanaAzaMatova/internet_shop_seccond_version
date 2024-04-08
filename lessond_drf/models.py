from django.db import models

class InternetShop(models.Model):
    id = models.AutoField(primary_key=True)
    add_date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(max_length=100)
    sum_product = models.IntegerField(default=0)

