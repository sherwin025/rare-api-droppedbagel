from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rareapi.models.subscription import Subscription

class SubscriptionView(ViewSet):
    def retrieve(self, request, pk):
        sub = Subscription.objects.get(pk=pk)
        serializer = SubscriptionSerializer(sub)
        return Response(serializer.data)

    def list(self, request):
        subs = Subscription.objects.all()
        serializer = SubscriptionSerializer(subs, many=True)
        return Response(serializer.data)

    def create(self, request):
        subscription = Subscription.objects.create(
            follower_id=request.data["follower_id"],
            author_id=request.data["author_id"],
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