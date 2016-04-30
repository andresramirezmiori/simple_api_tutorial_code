from rest_framework import viewsets, status, filters
from blog.models import Post, Comentario
from blog.serializers import PostSerializer, ComentarioSerializer


class PostViewSet(viewsets.ModelViewSet):
    model = Post
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    #def perform_create(self, serializer):
    #	serializer.save(usuario=self.request.user)


class ComentarioViewSet(viewsets.ModelViewSet):
    model = Comentario
    serializer_class = ComentarioSerializer
    queryset = Comentario.objects.all()