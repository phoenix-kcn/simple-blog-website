from django.urls import include, path
from .views import PostListView, PostDetailView, PostCreateView

urlpatterns = [
    path('', PostListView.as_view(), name='home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'), # new
    path('post/new/', PostCreateView.as_view(), name='post_new'), # new
]
