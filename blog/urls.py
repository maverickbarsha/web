from django.contrib import admin
from django.template.context_processors import static
from django.urls import path, include

from blog.views import index, detail, auth,contact,next
from blog import views
from web import settings

app_name = "blog"


urlpatterns = [
    path('blogs/', index),
    path('<id>', detail),
    path('blogs/auth/', auth),
    path('/next',next),
    path('blogs/contact/', contact),
    path('search/', views.search, name="search"),
]



