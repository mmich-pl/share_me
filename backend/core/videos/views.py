from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .serializers import PostSerializer
from .models import Post


# Create your views here.


class PostsView(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    permission_classes = (AllowAny,)
    # http_method_names = ['GET', ]
    queryset = Post.objects.all()

    def list(self, request, **kwargs):
        serializer = self.serializer_class(self.queryset, many=True)
        return Response(serializer.data)

    def retrive(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.serializer_class(instance=instance)
        return Response(serializer.data)
