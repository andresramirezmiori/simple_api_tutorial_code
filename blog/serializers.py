from django.contrib.auth.models import User
from rest_framework import serializers
from blog.models import Post, Comentario


class PostSerializer(serializers.HyperlinkedModelSerializer):
    usuario = serializers.PrimaryKeyRelatedField(required=False, read_only=True)
    class Meta:
        model = Post
        fields = ('id', 'url', 'titulo', 'texto', 'fecha_creacion', 'usuario', 'comentarios')
        # extra_kwargs = {
        #    'url': {'view_name': 'blog:post-detail'}
        #    }


class ComentarioSerializer(serializers.HyperlinkedModelSerializer):
    usuario = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=False)

    class Meta:
        model = Comentario
        fields = ('id', 'url', 'texto', 'post', 'fecha_creacion', 'usuario')
