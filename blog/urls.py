from django.urls import path
from blog.views import BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView

app_name = "blog"

urlpatterns = [
    path("blog/article_list/", BlogListView.as_view(), name="article_list"),
    path("blog/article/<int:pk>/", BlogDetailView.as_view(), name="article_detail"),
    path("blog/article/new/", BlogCreateView.as_view(), name="article_create"),
    path("blog/article/<int:pk>/update/", BlogUpdateView.as_view(), name="article_update"),
    path("blog/article/<int:pk>/delete/", BlogDeleteView.as_view(), name="article_delete"),
    ]
