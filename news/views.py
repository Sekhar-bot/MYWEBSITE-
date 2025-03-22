from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from .models import Article
from .forms import ArticleForm
from django.shortcuts import render, get_object_or_404
from django.shortcuts import render
from .models import Advertisement


from django.shortcuts import render
from .models import Article, Advertisement
from django.db import models  # Add this import at the top of views.py
from django.shortcuts import render
from .models import Article, Advertisement

def home(request):
    articles = Article.objects.all().order_by('-published_at')
    
    # Query ads by their placement
    top_ads = Advertisement.objects.filter(is_active=True, placement='top')
    inline_ads = Advertisement.objects.filter(is_active=True, placement='inline')
    bottom_ads = Advertisement.objects.filter(is_active=True, placement='bottom')
    main_ads = Advertisement.objects.filter(is_active=True, placement='main')
    
    # Keep track of which ads are displayed (for impression tracking)
    displayed_ads = list(top_ads) + list(inline_ads) + list(bottom_ads) + list(main_ads)
    ad_ids = [ad.id for ad in displayed_ads]
    
    # Increment impression counter for displayed ads
    Advertisement.objects.filter(id__in=ad_ids).update(impressions=models.F('impressions') + 1)
    
    context = {
        'articles': articles,
        'top_ads': top_ads,
        'inline_ads': inline_ads,
        'bottom_ads': bottom_ads,
        'main_ads': main_ads,
        # Keep the original 'ads' for backward compatibility
        'ads': Advertisement.objects.filter(is_active=True)
    }
    
    return render(request, 'home.html', context)


@login_required(login_url='login')
def add_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            return redirect('home')
    else:
        form = ArticleForm()
    return render(request, 'add_article.html', {'form': form})

def login_view(request):
    return auth_views.LoginView.as_view(template_name='login.html')(request)

def logout_view(request):
    logout(request)  # Log out the user
    return render(request, 'logout.html')  # Show logout page with buttons


def read_more(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    return render(request, 'read_more.html', {'article': article})



from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Article

@login_required(login_url='login')
def profile(request):
    return render(request, 'profile.html', {'user': request.user})


@login_required
def delete_article(request, article_id):
    article = get_object_or_404(Article, id=article_id, author=request.user)
    
    if request.method == "POST":
        article.delete()
        return redirect('profile')

    return redirect('profile')


from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Article  # Ensure your Article model is imported

@login_required
def profile(request):
    articles = Article.objects.filter(author=request.user)  # Fetch only user’s articles
    return render(request, 'profile.html', {'articles': articles})



from django.shortcuts import render, get_object_or_404
from .models import Article

def category_view(request, category):
    articles = Article.objects.filter(category=category).order_by('-published_at')
    return render(request, 'category.html', {'articles': articles, 'category': category})




from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from .models import Article
from django.contrib.auth.models import AnonymousUser

@csrf_exempt
def like_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)

    if isinstance(request.user, AnonymousUser):
        return JsonResponse({"error": "Login required"}, status=403)

    if request.user in article.likes.all():
        article.likes.remove(request.user)  # Unlike
    else:
        article.likes.add(request.user)  # Like
        article.dislikes.remove(request.user)  # Remove dislike if exists

    return JsonResponse({"likes": article.likes.count(), "dislikes": article.dislikes.count()})

@csrf_exempt
def dislike_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)

    if isinstance(request.user, AnonymousUser):
        return JsonResponse({"error": "Login required"}, status=403)

    if request.user in article.dislikes.all():
        article.dislikes.remove(request.user)  # Remove dislike
    else:
        article.dislikes.add(request.user)  # Dislike
        article.likes.remove(request.user)  # Remove like if exists

    return JsonResponse({"likes": article.likes.count(), "dislikes": article.dislikes.count()})




from django.shortcuts import render

def about_page(request):
    return render(request, 'about.html')



from django.shortcuts import render
from .models import Project

def projects_view(request):
    projects = Project.objects.all()
    return render(request, 'projects.html', {'projects': projects})





from django.shortcuts import render
from .models import Notification  # Assuming you have a Notification model

def notifications_page(request):
    notifications = Notification.objects.all().order_by('-timestamp')  # Latest first
    return render(request, 'notifications.html', {'notifications': notifications})
