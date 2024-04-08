from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from lessond_drf.serializer import NewsSerializerInternetShop
from .models import InternetShop

from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from rest_framework.decorators import action

# Create your views here.
class ListInfo(APIView):
    def get(self, request, format=None):
        article_titles = [article for article in InternetShop.objects.all()]
        serializer = NewsSerializerInternetShop(article_titles, many=True)
        return Response(serializer.data)

class NewsViewSet(viewsets.ModelViewSet):
    queryset = InternetShop.objects.all()
    serializer_class = NewsSerializerInternetShop
    # permission_classes = (IsAuthenticated,)

    # def list(self, request):
    #     response = InternetShop.objects.all()
    #     serialize = NewsSerializerInternetShop(response, many=True)
    #     if len(response) > 0:
    #         return Response(serialize.data)
    #     else:
    #         return Response(False)
    #
    # def category(self, request):
    #     response = InternetShop.objects.filter(category=request.data['category'])
    #     serialize = NewsSerializerInternetShop(response, many=True)
    #     if len(response) > 0:
    #         return Response(serialize.data)
    #     else:
    #         return Response(False)
    #
    # def update(self, request):
    #     print(request.data)
    #     InternetShop.objects.filter(id=int(request.data['id'])).update(description=request.data['description'])
    #     return Response("Value is changed")
    #
    # def create(self, request):
    #     print(request.data)
    #     InternetShop.objects.create(id=int(request.data['id']),
    #                                 title=request.data['title'],
    #                                 description=request.data['description'],
    #                                 category=request.data['category'],
    #                                 sum_product=int(request.data['sum_product']),)
    #     return Response("Value is added")
    #
    # @action(detail=False, methods=['post'])
    # def delete(self, request, format=None):
    #     InternetShop.objects.filter(id = request.data['id']).delete()
    #     return Response(request.data['id'] + ' deleted')


