from django.shortcuts import render
from django.db.models import Q
# Create your views here.
from blog.models import Article,Category,Author

def get_payload(request, title=""):
    return {
        "title": title,
        "categories": Category.objects.filter(active=True),
        "author": Author.objects.filter(active=True),
    }

def index(req):
    blogs=Article.objects.all()
    dict={'data':blogs}
    return render(req,"blog/index.html",dict)


def detail(req,id):
    blogs=Article.objects.all()
    dict={'data':blogs}
    return render(req,"blog/detail.html",dict)
def auth(req):
    author = Article.objects.all()
    dict = {'data': author}
    return render(req, "blog/auth.html", dict)
def contact(req):
    author=Article.objects.all()
    dict={'data':author}
    return render(req, "blog/contact.html", dict)

def next(req):
    blogs=Article.objects.all()
    dict={'data':blogs}
    return render(req,"/next.html",dict)

def search(request):
    if request.method == 'POST':
        query= request.GET.get('q')
        # submitbutton= request.GET.get('submit')
        if query is not None:
            lookups= Q(title__icontains=query) | Q(content__icontains=query)

            results= Article.objects.filter(lookups)

            context={'results': results, "q":query}

            return render(request, 'blog/search-result.html', context)
        else:
            return render(request, 'blog/search.html')
    else:
        return render(request, 'blog/search.html')

