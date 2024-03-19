from rest_framework import serializers
from .models import Article, ArticleImage, ArticleVideo


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleImage
        fields = ['image']  # Adjust if you want other image-related fields


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleVideo
        fields = ['video']

class ArticleSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, read_only=True)
    videos = VideoSerializer(many=True,read_only=True)
    tags = serializers.SerializerMethodField()
    class Meta:
        model = Article
        fields = ('id','ArticleTitle','introduction','content','date_added','slug','images','videos','tags')

    def get_tags(self, obj):
        return [tag.name for tag in obj.tags.all()]