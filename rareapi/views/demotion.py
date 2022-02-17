from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rareapi.models import Demotion, theUser

class DemotionView(ViewSet):
    def retrieve(self, request, pk):
        demotion = Demotion.objects.get(pk=pk)
        serializer = DemotionSerializer(demotion)
        return Response(serializer.data)

    def list(self, request):
        demotions = Demotion.objects.all()

        serializer = DemotionSerializer(demotions, many=True)
        return Response(serializer.data)

    def create(self, request):
        user = theUser.objects.get(pk=request.data['userId'])
        first_approver = theUser.objects.get(user = request.auth.user)

        demotion = Demotion.objects.create(
            user=user,
            first_approver=first_approver,
            deactivate = request.data['deactivate'],
            demote = request.data['demote']
        )
        serializer = DemotionSerializer(demotion)
        return Response(serializer.data)

    def destroy(self, request, pk):
        demotion = Demotion.objects.get(pk=pk)
        demotion.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)



class DemotionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Demotion
        fields = '__all__'
        depth = 1