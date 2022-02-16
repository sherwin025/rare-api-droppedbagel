from django.forms import ValidationError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rareapi.models import Reaction, Post, PostReaction
from rareapi.models.user import theUser


class PostReactionView(ViewSet):
    """Rare post_reactions"""

    def retrieve(self, request, pk=None):
        """Handle GET requests for single post_reaction

        Returns:
            Response -- JSON serialized post_reaction
        """
        try:
            post_reaction = PostReaction.objects.get(pk=pk)
            serializer = PostReactionSerializer(post_reaction)
            return Response(serializer.data)
        except PostReaction.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND) 


    def list(self, request):
        """Handle GET requests to get all post_reactions

        Returns:
            Response -- JSON serialized list of post_reactions
        """
        post_reactions = PostReaction.objects.all()
        serializer = PostReactionSerializer(post_reactions, many=True)
        return Response(serializer.data)


    def create(self, request):
        """Handle POST request to create new post_reaction

        Returns:
            Response -- JSON serialized post_reaction
        """
        
        post=Post.objects.get(pk=request.data['post_id'])
        reaction=Reaction.objects.get(pk=request.data['reaction_id'])
        user = theUser.objects.get(user = request.auth.user)
        
        post_reaction = PostReaction.objects.create(
            user = user,
            post = post,
            reaction = reaction
        )
        try:
            post_reaction.save()
            serializer = PostReactionSerializer(post_reaction)
            return Response (serializer.data, status=status.HTTP_201_CREATED)
        except ValidationError as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_400_BAD_REQUEST)


    def update(self, request, pk=None):
        """Handle PUT request for a single reaction

        Returns:
            No content, 204 status.
        """
        try:
            post = Post.objects.get(pk=request.data['post_id'])
            reaction = Reaction.objects.get(pk=request.data['reaction_id'])
            
            post_reaction = PostReaction.objects.get(pk=pk)
            post_reaction.post = post
            post_reaction.reaction = reaction
            post_reaction.save()
            return Response(None, status=status.HTTP_204_NO_CONTENT)
        except PostReaction.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_400_BAD_REQUEST)
        except ValidationError as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_400_BAD_REQUEST)


    def destroy(self, request, pk=None):
        """Handle DELETE request for a single post_reaction

        Returns:
            No content, 204 status.
        """
        try:
            post_reaction = PostReaction.objects.get(pk=pk)
            post_reaction.delete()
            return Response(None, status=status.HTTP_204_NO_CONTENT)
        except PostReaction.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_400_BAD_REQUEST)


class PostReactionSerializer(serializers.ModelSerializer):
    """JSON serializer for post_reaction
    """
    class Meta:
        model = PostReaction
        fields = ('id', 'user', 'post', 'reaction')
        depth = 1
