"""
URL configuration for news_aggregator project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from news.views import home, add_article , logout_view, read_more , profile , delete_article , category_view , like_article , dislike_article , about_page, projects_view  # ✅ Import the new views

urlpatterns = [
    path('admin/', admin.site.urls),  # ✅ Add this line to enable Django Admin
    path('', home, name='home'),
    path('add-article/', add_article, name='add_article'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', logout_view, name='logout'),
    path('read-more/<int:article_id>/', read_more, name='read_more'),
    path('profile/', profile, name='profile'),
    path('delete-article/<int:article_id>/', delete_article, name='delete_article'),# New Profile Page
    path('category/<str:category>/', category_view, name='category_view'),
    path('like/<int:article_id>/', like_article, name='like_article'),
    path('dislike/<int:article_id>/', dislike_article, name='dislike_article'),
    path('projects/', projects_view, name='projects'),
    path('about/', about_page, name='about'),
    
]

# ✅ Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
