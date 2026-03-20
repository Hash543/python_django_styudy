from django.urls import path
from .views import BlogView, DetailView

urlpatterns = [
    path('', BlogView.as_view(), name='index'),
    path('<int:id>/', DetailView.as_view(), name='detail'),
]