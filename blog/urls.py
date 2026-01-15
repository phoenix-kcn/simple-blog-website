from django.urls import include, path
from .views import ( 
    PostListView, 
    PostDetailView, 
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
)
urlpatterns = [
    path('', PostListView.as_view(), name='home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'), # new
    path('post/new/', PostCreateView.as_view(), name='post_new'), # new
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post_update'), # new
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'), # new
]
