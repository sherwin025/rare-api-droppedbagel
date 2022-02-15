"""View module for handling requests about game types"""
from django.forms import ValidationError
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rareapi.models import Tag


class TagView(ViewSet):
    """Level up game types"""

    def retrieve(self, request, pk=None):
        """Handle GET requests for single tag

        Returns:
            Response -- JSON serialized tag
        """
        try:
            tag = Tag.objects.get(pk=pk)
            serializer = TagSerializer(tag)
            return Response(serializer.data)
        except Tag.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND) 


    def list(self, request):
        """Handle GET requests to get all tags

        Returns:
            Response -- JSON serialized list of tags
        """
        tags = Tag.objects.order_by('label')
        serializer = TagSerializer(tags, many=True)
        return Response(serializer.data)
    
    
    def create(self, request):
        """Handle POST request to create new tag

        Returns:
            Response -- JSON serialized tag
        """
        tag = Tag.objects.create(
            label=request.data['label']
        )
        try:
            tag.save()
            serializer = TagSerializer(tag)
            return Response (serializer.data, status=status.HTTP_201_CREATED)
        except ValidationError as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_400_BAD_REQUEST)
    
    
    def destroy(self, request, pk=None):
        """Handle DELETE request for a single tag

        Returns:
            No content, 204 status.
        """
        try:
            tag = Tag.objects.get(pk=pk)
            tag.delete()
            return Response(None, status=status.HTTP_204_NO_CONTENT)
        except Tag.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_400_BAD_REQUEST)


    def update(self, request, pk=None):
        """Handle PUT request for a single tag

        Returns:
            No content, 204 status.
        """
        try:
            tag = Tag.objects.get(pk=pk)
            tag.label = request.data['label']
            tag.save()
            return Response(None, status=status.HTTP_204_NO_CONTENT)
        except Tag.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_400_BAD_REQUEST)
        except ValidationError as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_400_BAD_REQUEST)


class TagSerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    class Meta:
        model = Tag
        fields = ('id', 'label')
