from django.views.generic import (ListView, DetailView,
                                  CreateView, UpdateView,
                                  DeleteView)
from django.urls import reverse_lazy
from .models import BlogPost


class BlogPostListView(ListView):
    model = BlogPost
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        """Фильтрация только опубликованных статей"""
        queryset = super().get_queryset()
        return queryset.filter(is_published=True).order_by('-created_at')


class BlogPostDetailView(DetailView):
    model = BlogPost
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

    def get_object(self, queryset=None):
        """Увеличение счетчика просмотров при каждом открытии статьи"""
        obj = super().get_object(queryset)
        obj.views_count += 1
        obj.save()
        return obj


class BlogPostCreateView(CreateView):
    model = BlogPost
    template_name = 'blog/post_form.html'
    fields = ['title', 'content', 'preview', 'is_published']
    success_url = reverse_lazy('blog:post_list')


class BlogPostUpdateView(UpdateView):
    model = BlogPost
    template_name = 'blog/post_form.html'
    fields = ['title', 'content', 'preview', 'is_published']

    def get_success_url(self):
        """Перенаправление на просмотр отредактированной статьи"""
        return reverse_lazy('blog:post_detail', kwargs={'pk': self.object.pk})


class BlogPostDeleteView(DeleteView):
    model = BlogPost
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('blog:post_list')