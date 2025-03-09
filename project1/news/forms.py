from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content', 'category', 'sentiment', 'source_url', 'image']
    image = forms.ImageField(required=False)
