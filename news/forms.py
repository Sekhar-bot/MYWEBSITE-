from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content', 'category', 'sentiment', 'source_url', 'image']
        widgets = {
            'category': forms.Select(attrs={'class': 'form-control'}),  # Bootstrap styling
        }
# Compare this snippet from project1/news/forms.py:
    image = forms.ImageField(required=False)
