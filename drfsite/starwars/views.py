from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Person
from .serializers import StarwarsSerializer


class StarwarsAPIView(APIView):
    def get(self, request):
        queryset = Person.objects.all().values()
        return Response({'posts': list(queryset)})

    def post(self, request):
        post_new = Person.objects.create(
            title=request.data['title'],
            content=request.data['content'],
            cat_id=request.data['cat_id']
        )
        return Response({'post': model_to_dict(post_new)})

# class StarwarsAPIView(generics.ListAPIView):
#     queryset = Person.objects.all()
#     serializer_class = StarwarsSerializer
