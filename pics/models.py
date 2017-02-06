from django.db import models

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}/{2}'.format(instance.album.user.id, instance.album.id, filename)

class Album(models.Model):
    user = models.ForeignKey('auth.User', related_name='albuns', on_delete=models.CASCADE)

    nome = models.CharField(max_length=50)
    descricao = models.CharField(max_length=200, null=True, default='')

    data_alteracao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%d - %s' % (self.id, self.nome)

    class Meta:
        ordering = ('nome',)

class Foto(models.Model):
    user = models.ForeignKey('auth.User', related_name='fotos', on_delete=models.CASCADE)

    album = models.ForeignKey(Album, related_name='fotos', on_delete=models.CASCADE)
    titulo = models.CharField(max_length=50)
    imagem = models.ImageField(upload_to=user_directory_path)

    data_alteracao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%d - %s' % (self.id, self.titulo)

    class Meta:
        ordering = ('data_alteracao',)
