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

    # Like & Dislike System
    likes = models.ManyToManyField(User, related_name='liked_articles', blank=True)
    dislikes = models.ManyToManyField(User, related_name='disliked_articles', blank=True)

    def total_likes(self):
        return self.likes.count()

    def total_dislikes(self):
        return self.dislikes.count()

    def __str__(self):
        return self.title


from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    link = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to='projects/', blank=True, null=True)

    def __str__(self):
        return self.title





from django.db import models

class Advertisement(models.Model):
    PLACEMENT_CHOICES = [
        ('top', 'Top Carousel'),
        ('inline', 'Between Articles'),
        ('bottom', 'Bottom Carousel'),
        ('main', 'Main Section'),
    ]
    
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='ads/')
    link = models.URLField()
    description = models.TextField(blank=True)
    placement = models.CharField(
        max_length=10, 
        choices=PLACEMENT_CHOICES, 
        default='main',
        help_text="Where this ad should appear on the page"
    )
    is_active = models.BooleanField(default=True)
    clicks = models.PositiveIntegerField(default=0, help_text="Number of times this ad was clicked")
    impressions = models.PositiveIntegerField(default=0, help_text="Number of times this ad was shown")
    
    class Meta:
        verbose_name = "Advertisement"
        verbose_name_plural = "Advertisements"
        ordering = ['-is_active', 'title']
    
    def __str__(self):
        return f"{self.title} ({self.get_placement_display()})"
    
    @property
    def click_through_rate(self):
        """Calculate the click-through rate (CTR) for this ad"""
        if self.impressions == 0:
            return 0
        return (self.clicks / self.impressions) * 100
    
    
    
    
    
