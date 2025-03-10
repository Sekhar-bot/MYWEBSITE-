from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from .models import Article
from .forms import ArticleForm
from django.shortcuts import render, get_object_or_404


def home(request):
    articles = Article.objects.all().order_by('-published_at')
    return render(request, 'home.html', {'articles': articles})

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
