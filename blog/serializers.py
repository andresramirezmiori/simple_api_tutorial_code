from django.contrib.auth.models import User
from rest_framework import serializers
from blog.models import Post, Comentario


class PostSerializer(serializers.HyperlinkedModelSerializer):
    usuario = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    class Meta:
        model = Post
        fields = ('id', 'url', 'titulo', 'texto', 'fecha_creacion', 'usuario', 'comentarios')
        # extra_kwargs = {
        #    'url': {'view_name': 'blog:post-detail'}
        #    }


class ComentarioSerializer(serializers.HyperlinkedModelSerializer):
    usuario = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    # def validate(self, data):
    #     """
    #     Check that the start is before the stop.
    #     """
    #     if data['coment'] and data['post']:
    #         raise serializers.ValidationError("El comentario no puede ser a un post y un comentario al mismo tiempo")
    #
    #     if not data['coment'] and not data['post']:
    #         raise serializers.ValidationError("Debe especificar un post o un comentario")
    #
    #     if self.instance.id and data['coment']:
    #         if self.instance.id == data['comment'].id:
    #             raise serializers.ValidationError("El comentario no puede ser a si mismo")
    #     return data

    class Meta:
        model = Comentario
        fields = ('id', 'url', 'texto', 'post', 'fecha_creacion', 'usuario')
