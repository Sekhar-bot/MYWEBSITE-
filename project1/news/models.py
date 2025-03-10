from django.db import models
from django.contrib.auth.models import User

class Article(models.Model):
    CATEGORY_CHOICES = [
        ('Technology', 'Technology'),
        ('Science', 'Science'),
        ('Health', 'Health'),
        ('Business', 'Business'),
        ('Sports', 'Sports'),
        ('Entertainment', 'Entertainment'),
    ]

    title = models.CharField(max_length=255)
    content = models.TextField()
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES, default='Technology')
    sentiment = models.CharField(max_length=50, null=True, blank=True)
    source_url = models.URLField()
    published_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)  # Link to user
    image = models.ImageField(upload_to='article_images/', max_length=255, null=True, blank=True)

    def __str__(self):
        return self.title
# Compare this snippet from project1/news/views.py:
