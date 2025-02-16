from django.urls import reverse_lazy, reverse
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Blog
from .templates.blog.forms import BlogForm


class BlogListView(ListView):
    model = Blog
    template_name = 'blog/article_list.html'
    context_object_name = 'articles'

    def get_queryset(self):
        return Blog.objects.filter(is_published=True)


class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog/article_detail.html'
    context_object_name = 'article'

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.counter +=1
        self.object.save()
        return self.object


class BlogCreateView(CreateView):
    model = Blog
    form_class = BlogForm
    template_name = 'blog/article_form.html'
    success_url = reverse_lazy('blog:article_list')


class BlogUpdateView(UpdateView):
    model = Blog
    form_class = BlogForm
    template_name = 'blog/article_form.html'
    success_url = reverse_lazy('blog:article_list')

    def get_success_url(self):
        return reverse('blog:article_detail', args=[self.kwargs.get('pk')])


class BlogDeleteView(DeleteView):
    model = Blog
    template_name = 'blog/article_confirm_delete.html'
    success_url = reverse_lazy('blog:article_list')
