from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rareapi.models.subscription import Subscription
from rareapi.models.user import theUser

class SubscriptionView(ViewSet):
    def retrieve(self, request, pk):
        sub = Subscription.objects.get(pk=pk)
        serializer = SubscriptionSerializer(sub)
        return Response(serializer.data)

    def list(self, request):
        subs = Subscription.objects.all()
        author = request.query_params.get('author', None)
        if author is not None:
            subs = subs.filter(author=author)
        serializer = SubscriptionSerializer(subs, many=True)
        return Response(serializer.data)

    def create(self, request):
        follower = theUser.objects.get(pk=request.data['follower'])
        author = theUser.objects.get(pk=request.data["author"])

        subscription = Subscription.objects.create(
            follower=follower,
            author=author,
            created_on=request.data["created_on"]
        )
        serializer = SubscriptionSerializer(subscription)
        return Response(serializer.data)

    def destroy(self, request, pk):
        sub = Subscription.objects.get(pk=pk)
        sub.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)



class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = '__all__'
        depth = 1