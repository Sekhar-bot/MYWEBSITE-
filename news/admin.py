from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Article

admin.site.register(Article)


from django.contrib import admin
from .models import Project

admin.site.register(Project)



from django.contrib import admin
from .models import Advertisement

admin.site.register(Advertisement)
