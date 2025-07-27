from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .forms import BlogForm
from .models import Blog


class BlogListView(ListView):
    model = Blog
    template_name = 'blog/blog_list.html'
    context_object_name = 'blogs'

    def get_queryset(self):
        return Blog.objects.filter(is_published=True)


class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog/blog_detail.html'
    context_object_name = 'blog'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        obj.views_count += 1
        obj.save(update_fields=['views_count'])
        return obj


class BlogCreateView(CreateView):
    model = Blog
    form_class = BlogForm  # ← используем форму с валидацией
    template_name = 'blog/blog_form.html'
    success_url = reverse_lazy('blog:post_list')


class BlogUpdateView(UpdateView):
    model = Blog
    form_class = BlogForm  # ← используем форму с валидацией
    template_name = 'blog/blog_form.html'

    def get_success_url(self):
        return reverse('blog:blog_detail', kwargs={'pk': self.object.pk})


class BlogDeleteView(DeleteView):
    model = Blog
    template_name = 'blog/blog_confirm_delete.html'
    success_url = reverse_lazy('blog:post_list')
