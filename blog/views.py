from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views import View
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.permissions import (
  IsAuthenticated,
  IsAuthenticatedOrReadOnly,
  IsAdminUser,
  AllowAny
)
from .permission import IsAuthorOrReadOnly
from .serializers import PostSerializer
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
        post = get_object_or_404(Post, id=id)
        print(f'id: {id}')
        return render(request, 'blog/detail.html', {'post': post})

# class PostListAPI(APIView):
#     # GET /api/posts/
#     def get(self, request):
#         posts = Post.objects.all()
#         serializer = PostSerializer(posts, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     # POST /api/posts/
#     def post(self, request):
#         serializer = PostSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# class PostDetailAPI(APIView):
#     # GET /api/posts/1/
#     def get(self, request, id):
#         post = get_object_or_404(Post, id=id)
#         serializer = PostSerializer(post)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     # PUT /api/posts/1/)
#     def put(self, request, id):
#         post = get_object_or_404(Post, id=id)
#         serializer = PostSerializer(post, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     # DELETE /api/posts/1/
#     def delete(self, request, id):
#         post = get_object_or_404(Post, id=id)
#         post.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # permission_classes = [IsAuthenticated]
    # permission_classes = [AllowAny]
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)