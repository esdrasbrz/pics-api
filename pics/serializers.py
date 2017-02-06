from rest_framework import serializers
from .models import Album, Foto

class FotoSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Foto
        fields = ('id', 'user', 'album', 'titulo', 'imagem', 'data_alteracao')


class AlbumSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    fotos = FotoSerializer(many=True, read_only=True)

    class Meta:
        model = Album
        fields = ('id', 'user', 'nome', 'descricao', 'fotos', 'data_alteracao')
