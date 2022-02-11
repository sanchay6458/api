from rest_framework import serializers
from blog.models import Blog

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ('id','title', 'subtitle', 'author', 'body', 'header_image')
        
class BlogSerializerCreate(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ('title', 'subtitle','author', 'body', 'header_image')