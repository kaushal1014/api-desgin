from django.shortcuts import render
from django.http import HttpResponse
from .models import Article
from .serializers import ArticleSerializer
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, mixins, status
# Create your views here.

class ArticleAPI(APIView):
    authentication_classes = [ TokenAuthentication ]
    permission_classes = [IsAuthenticated]
    def get(self, request):
        article = Article.objects.all()
        serializer=ArticleSerializer(article, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer=ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ArticleDetail(APIView):
    def get_object(self, pk):
        try:
            return Article.objects.get(id=pk)
        except Article.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    
    def get(self, request,pk):
        article= self.get_object(pk)
        serializer=ArticleSerializer(article)
        return Response(serializer.data)

    def put(self,request, pk):
        article= self.get_object(pk)
        serializer=ArticleSerializer(article,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        article= self.get_object(pk)
        article.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)

"""
class Authentication(APIView):


    def get(self, request, format=None):
        content = {
            'user': str(request.user),  # `django.contrib.auth.User` instance.
            'auth': str(request.auth),  # None
        }
        return Response(content)

"""
class GenericAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.UpdateModelMixin, mixins.CreateModelMixin, mixins.DestroyModelMixin, mixins.RetrieveModelMixin):
    serializer_class = ArticleSerializer
    queryset= Article.objects.all()

    lookup_field="pk"

    def get(self, request, pk=None):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request,pk)

    def post(self, request, pk=None):
        return self.create(request,pk)
    
    def delete(self, request, pk=None):
        return self.destroy(request,pk)
    
    def put(self, request, pk=None):
        return self.update(request,pk)
    



