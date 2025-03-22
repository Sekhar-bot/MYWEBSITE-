from django.urls import path
from .views import home, add_article 



urlpatterns = [
    path('', home, name='home'),
    path('add/', add_article, name='add_article'),
   
    
]
# Compare this snippet from news_aggregator/news/views.py: