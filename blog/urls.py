from django.urls import include, path
from .views import ( 
    PostListView, 
    PostDetailView, 
    PostCreateView,
    PostUpdateView,
)
urlpatterns = [
    path('', PostListView.as_view(), name='home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'), # new
    path('post/new/', PostCreateView.as_view(), name='post_new'), # new
    path('post/<int:pk>/edit/', PostUpdateView.as_view(), name='post_edit'), # new
]
