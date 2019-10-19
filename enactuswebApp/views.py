from urllib.parse import quote_plus
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator
from django.utils import timezone
from .models import Post,ImageUpload

def home(request):
    # queryset = Post.objects.all()
    # context ={
    #     'object_list':queryset,
    #     'title':'Enactus Latest Posts'
    # }
    return render(request, 'enactus-template/index.html')
    
def about(request):
    return render(request, 'enactus-template/about.html')

def gallary(request):
    queryset = ImageUpload.objects.all()
    context ={
        'image_list':queryset,
        'title':'Enactus UDS Our Gallary'
    }
    return render(request, 'enactus-template/gallary.html',context)

def blog(request):
    queryset = Post.objects.filter(draft=False).all()
   
    query = request.GET.get("q")
    if query:
        queryset = queryset.filter(Q(title__icontains=query) | Q(content__icontains=query))
    paginator = Paginator(queryset, 5)
    page = request.GET.get('page')
    try:
       posts = paginator.get_page(page)
    except PageNotAnInteger:
        posts = paginator.get_page(1)
    except EmptyPage:
        posts = paginator.get_page(Paginator.num_pages)

    context ={
        #'post':posts,
        'object_list':posts,
        'title':'Enactus Latest Posts'
    }
    return render(request, 'enactus-template/blog.html', context)

def blog_detail(request,slug_text):
    #instance = get_object_or_404(Post, slug=slug_text)
    q = Post.objects.filter(slug=slug_text)
    if q.exists():
        q = q.first()
    else:
        return HttpResponse("Page not found") 
    share_string = quote_plus(q.content)
      
    # #instance = Post.objects.all() 
    context ={
        'title':q.title,
        #'title' : instance.title,
        'share_string':share_string,
         'instance':q
        #'instance': instance
    }
    return render(request, 'enactus-template/post_detail.html', context)
