from django import forms
from .models import Article, Tag


class ArticleForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.all(), widget=forms.CheckboxSelectMultiple)
    class Meta:
        model = Article
        fields = ['ArticleTitle','introduction', 'content', 'tags']



class SearchForm(forms.Form):
    search_query = forms.CharField(max_length=100, label='Search')

