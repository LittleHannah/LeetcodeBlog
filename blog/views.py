from django.shortcuts import render

# Create your views here.
import markdown
from django.shortcuts import render, get_object_or_404
from .models import Post


def index(request):
    post_list = Post.objects.all().order_by('-created_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})

def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    # 记得在顶部引入 markdown 模块
    post.answer = markdown.markdown(post.answer,
                                  extensions=[
                                     'markdown.extensions.extra',
                                     'markdown.extensions.codehilite',
                                     'markdown.extensions.toc',
                                  ])

    return render(request, 'blog/detail.html', context={'post': post})

