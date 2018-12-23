from django.contrib import admin
from blog.models import Article,Author,Category
class ArticleAdmin(admin.ModelAdmin):
    list_display = ["title","author","created","category","published"]
    list_filter = ["title","author","category","created"]
    search_fields = ["title"]
# Register your models here.
admin.site.register(Article, ArticleAdmin)
admin.site.register(Author)
admin.site.register(Category)
