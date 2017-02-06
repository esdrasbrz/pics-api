from .models import Album, Foto
from .serializers import AlbumSerializer, FotoSerializer
from .permissions import IsOwnerOrReadOnly
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework.decorators import detail_route
from rest_framework import generics, permissions, renderers, viewsets, serializers
from django.contrib.auth.models import User
from wsgiref.util import FileWrapper


class AlbumViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class FotoViewSet(viewsets.ModelViewSet):
    queryset = Foto.objects.all()
    serializer_class = FotoSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly)

    def perform_create(self, serializer):
        album = serializer.validated_data['album']

        if self.request.user.id == album.user_id:
            serializer.save(user=self.request.user)
        else:
            raise serializers.ValidationError('Usuario nao tem acesso ao album')

    @detail_route(methods=['GET'])
    def get_file(self, request, *args, **kwargs):
        foto = self.get_object()

        with open(foto.imagem.path, 'rb') as img:
            response = HttpResponse(FileWrapper(img), content_type='image/jpeg')

            return response
