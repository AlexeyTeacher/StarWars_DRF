from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Person
from .serializers import PersonSerializer


class StarwarsAPIList(generics.ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class StarwarsAPIUpdate(generics.UpdateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class StarwarsAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

# class StarwarsAPIView(APIView):
#     def get(self, request):
#         queryset = Person.objects.all().values()
#         return Response({'posts': PersonSerializer(queryset, many=True).data})
#
#     def post(self, request):
#         serializer = PersonSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#
#         return Response({'post': serializer.data})
#
#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error": "Method PUT not allowed"})
#         try:
#             instance = Person.objects.get(pk=pk)
#         except Exception as ex:
#             return Response({"error": str(ex)})
#         serializer = PersonSerializer(data=request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({"post": serializer.data})
#
#     def delete(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error": "Method DELETE not allowed"})
#         try:
#             record = Person.objects.get(pk=pk)
#             record.delete()
#         except Exception as ex:
#             return Response({"error": str(ex)})
#
#         return Response({"post": f"delete post №{pk}"})

