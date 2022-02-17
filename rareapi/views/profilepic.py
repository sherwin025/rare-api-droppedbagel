from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from models import userPicture
import uuid


class ProfilePicView(ViewSet):

    def create(self, request):
        profile_pic = userPicture()
        format, imgstr = request.data["user_image"].split(';base64,')
        ext = format.split('/')[-1]
        data = ContentFile(base64.b64decode(imgstr), name=f'{request.data["user_id"]}-{uuid.uuid4()}.{ext}')
        profile_pic.profile_pic = data
        serialized = ProfilePicSerializer(profile_pic)
        serialized.save()
        # follower = theUser.objects.get(pk=request.data['follower'])
        # author = theUser.objects.get(pk=request.data["author"])

        # subscription = Subscription.objects.create(
        #     follower=follower,
        #     author=author
        # )
        # serializer = ProfilePicSerializer(subscription)
        # return Response(serializer.data)



class ProfilePicSerializer(serializers.ModelSerializer):
    class Meta:
        model = userPicture
        fields = '__all__'
        depth = 1