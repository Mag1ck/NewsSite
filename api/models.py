from django.db import models
from django.urls import reverse
from django.utils.text import slugify

class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Article(models.Model):
    ArticleTitle = models.CharField(max_length=200, unique=True)
    introduction = models.TextField()
    content = models.TextField()
    date_added = models.DateTimeField(auto_now=True)
    slug = models.SlugField(default="", editable=False)
    tags = models.ManyToManyField(Tag)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.ArticleTitle)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('article-detail', args=[self.slug])

    def __str__(self):
        return self.ArticleTitle

class ArticleImage(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='static')  # Store images in 'article_images'


class ArticleVideo(models.Model):
    article = models.ForeignKey(Article,on_delete=models.CASCADE,related_name='videos')
    video = models.FileField(upload_to='static')