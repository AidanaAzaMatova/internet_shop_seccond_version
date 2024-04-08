from rest_framework import serializers
from .models import InternetShop

class NewsSerializerInternetShop(serializers.ModelSerializer):
    class Meta:
        model = InternetShop
        fields = (
            'id',
            'add_date',
            'title',
            'description',
            'category',
            'sum_product'
        )

