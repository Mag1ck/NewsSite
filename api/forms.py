from django import forms
from .models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['ArticleTitle', 'introduction', 'content', 'image']


class SearchForm(forms.Form):
    search_query = forms.CharField(max_length=100, label='Search')
