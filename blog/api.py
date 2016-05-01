import copy
from django.core.urlresolvers import reverse
from blog.models import Post, Comentario
from blog.serializers import PostSerializer, ComentarioSerializer
from rest_framework import viewsets, status, filters, serializers
from rest_framework.decorators import detail_route
from rest_framework.response import Response


class PostViewSet(viewsets.ModelViewSet):
    model = Post
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)

    def _create_comentario(self, request, pk):
        #se obtiene la url del post, ya que el serializer del comentario espera recibir una url
        post_url = reverse('post-detail', kwargs={'pk': pk})
        data = copy.copy(request.data)
        data['post'] = post_url

        serializer = ComentarioSerializer(data=data, context={'request': request})
        if serializer.is_valid(raise_exception=True):
            #esto reemplaza el perfome_create del ComentarioViewSet
            serializer.save(usuario=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    def _list_comentarios(self, request, pk):
        post = Post.objects.get(pk=pk)
        serializer = ComentarioSerializer(post.comentarios, many=True, context={"request": request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    @detail_route(methods=['get', 'post'])
    def comentarios(self, request, pk=None):
        #El comentario debe ser realizado a un post y el post debe ser un post existente
        if pk is None:
            raise serializers.ValidationError("los comentarios deben crearse para un post")
        if not Post.objects.filter(pk=pk).exists():
            raise serializers.ValidationError("El post especificado no existe")

        if request.method =="POST":
            return self._create_comentario(request, pk)
        else:
            return self._list_comentarios(request, pk)



class ComentarioViewSet(viewsets.ReadOnlyModelViewSet):
    model = Comentario
    serializer_class = ComentarioSerializer
    queryset = Comentario.objects.all()