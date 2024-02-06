from django.db import models

class Article(models.Model):
    ArticleTitle = models.CharField(max_length=200, unique=True)
    content = models.TextField()
    date_added = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='static')

    def __str__(self):
        return self.ArticleTitle,self.content,self.date_added

