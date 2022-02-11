from rest_framework import generics, permissions
from blog.models import Blog
from .serializers import BlogSerializer,BlogSerializerCreate
from .permissions import IsAuthorOrReadOnly



class BlogAPIView(generics.ListAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

class BlogDetailAPIView(generics.RetrieveAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    
class BlogCreateAPIView(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Blog.objects.get_queryset()
    serializer_class = BlogSerializerCreate

# class BlogUpdateAPIView(generics.RetrieveUpdateAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
#     queryset = Blog.objects.all()
#     serializer_class = BlogSerializer

# class BlogDeleteAPIView(generics.RetrieveDestroyAPIView):
#     permission_classes = (permissions.IsAuthenticated,)
#     queryset = Blog.objects.all()
#     serializer_class = BlogSerializer

class BlogDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

# Create your views here.
