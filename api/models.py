from django.db import models
from django.utils.text import slugify

class Article(models.Model):
    ArticleTitle = models.CharField(max_length=200, unique=True)
    content = models.TextField()
    date_added = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='static')
    slug = models.SlugField(default="", editable=False)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.ArticleTitle)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.ArticleTitle