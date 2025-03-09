from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from .models import Article
from .forms import ArticleForm


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
