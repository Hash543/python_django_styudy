from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views import View
from .models import Post
class BlogView(View):
    def get(self, request):
        posts = Post.objects.all()
        print(posts)
        return render(request, 'blog/index.html', {
            'posts': posts
        })
    def post(self, request):
        data = request.POST.get('title')
        return JsonResponse({'title': data})

class DetailView(View):
    def get(self, request, id):
        post = Post.objects.get(id=id)
        return render(request, 'blog/detail.html', {'post': post})
