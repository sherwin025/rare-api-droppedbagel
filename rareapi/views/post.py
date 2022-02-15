from socketserver import ThreadingUDPServer
from wsgiref.util import setup_testing_defaults
from django.forms import ValidationError
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rareapi.models import Post, theUser
from django.db.models import Q
from datetime import datetime


class PostView(ViewSet):
    def retrieve(self, request, pk):
        try:
            post = Post.objects.get(pk=pk)
            serializer = PostSerializer(post)
            return Response(serializer.data)
        except Post.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        posts = Post.objects.filter(Q(approved="True") & Q(publication_date__lte=datetime.now())).order_by("-publication_date")
        search_title = self.request.query_params.get("search", None)
        search_cat = self.request.query_params.get("catfilter", None)
        search_tag = self.request.query_params.get("tagfilter", None)
        search_user = self.request.query_params.get("userfilter", None)
        if search_title is not None:
            posts = posts.filter(Q(title__contains=search_title))
        if search_cat is not None:
            posts = posts.filter(Q(category__contains=search_cat))
        if search_tag is not None:
            posts = posts.filter(Q(tag__contains=search_tag))
        if search_user is not None:
            posts = posts.filter(Q(user_id__id=search_user))
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    
    def destroy(self, request, pk):
        post = Post.objects.get(pk=pk)
        post.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    def update(self,request, pk):
        try: 
            post = Post.objects.get(pk=pk)
            serializer = PostSerializer(post, request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(None, status=status.HTTP_204_NO_CONTENT)
        except ValidationError as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_400_BAD_REQUEST)
        
    def create(self, request):
        try:
            serializer = CreatePostSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except ValidationError as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_400_BAD_REQUEST)
    


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"
        depth = 2

class CreatePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"