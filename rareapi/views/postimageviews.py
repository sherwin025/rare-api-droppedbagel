from django.forms import ValidationError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
import uuid
from rareapi.models.postimage import PostImage
from django.core.files.base import ContentFile
import base64


class PostImageView(ViewSet):

    def list(self, request):
        image = PostImage.objects.all()
       
        serializer = ImageSerializer(image, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk):
        image = PostImage.objects.get(pk=pk)
      
        format, imgstr = request.data["postimage"].split(';base64,')
        ext = format.split('/')[-1]
        data = ContentFile(base64.b64decode(imgstr), name=f'{request.data["post"]}-{uuid.uuid4()}.{ext}')
        serializer = ImageSerializer(image)
        serializer.save(postimage=data)
        return Response(serializer.data)

    def create(self, request):
        try:
            format, imgstr = request.data["postimage"].split(';base64,')
            ext = format.split('/')[-1]
            data = ContentFile(base64.b64decode(imgstr), name=f'{request.data["post"]}-{uuid.uuid4()}.{ext}')
            image = PostImage.objects.create(postimage=data, post_id=request.data["post"])
            return Response({}, status=status.HTTP_201_CREATED)
        except ValidationError as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk):
        image = PostImage.objects.get(pk=pk)
        image.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def update(self,request, pk):
        try: 
            format, imgstr = request.data["postimage"].split(';base64,')
            ext = format.split('/')[-1]
            data = ContentFile(base64.b64decode(imgstr), name=f'{request.data["post"]}-{uuid.uuid4()}.{ext}')
            image = PostImage.objects.get(pk=pk)
            image.postimage = data
            image.save()
            return Response(None, status=status.HTTP_204_NO_CONTENT)
        except ValidationError as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_400_BAD_REQUEST)



class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostImage
        fields = '__all__'

class CreateImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostImage
        fields = ('post',)