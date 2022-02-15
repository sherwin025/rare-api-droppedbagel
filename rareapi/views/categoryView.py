from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.decorators import action
from rareapi.models import Category, theUser


class CategoryView(ViewSet):

    def retrieve(self, request, pk):
        """Handle GET requests for single game type
        Returns:
            Response -- JSON serialized game type
        """
        try:
            category = Category.objects.get(pk=pk)
            serializer = CategorySerializer(category)
            return Response(serializer.data)
        except Category.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """Handle GET requests to get all categories
        Returns:
            Response -- JSON serialized list of game types
        """
        categories = Category.objects.all()
       
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle post requests to categories"""
        serializer = CategoryCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        """Update Category"""
        try:
            category = Category.objects.get(pk=pk)
            serializer = CategoryCreateSerializer(category, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(None, status=status.HTTP_204_NO_CONTENT)
        except Category.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk):
        """Delete Category"""
        category = Category.objects.get(pk=pk)
        category.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)





class CategorySerializer(serializers.ModelSerializer):
    """Serializer for categories"""
    class Meta:
        model = Category
        fields = ('id', 'label')
        depth = 1


class CategoryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['label']
