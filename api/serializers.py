from rest_framework import serializers
from taggit.serializers import TaggitSerializer, TagListSerializerField

from api.models import Category, Post


class PostCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class PostSerializer(TaggitSerializer, serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all()
    )
    tags = TagListSerializerField()

    class Meta:
        model = Post
        fields = '__all__'