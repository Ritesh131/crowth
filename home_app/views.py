from django.shortcuts import render
from django.views.generic import TemplateView
from home_app.models import *

# Create your views here.

class IndexView(TemplateView):
    template_name = 'static/index.html'

    def get_context_data(self, **kwargs):
        ctx = super(IndexView, self).get_context_data(**kwargs)
        ctx['blog'] = Blog.objects.all()[:3]
        return ctx


class BlogView(TemplateView):
    template_name = 'static/blog.html'

    def get_context_data(self, **kwargs):
        ctx = super(BlogView, self).get_context_data(**kwargs)
        ctx['blog'] = Blog.objects.filter(slug=kwargs.get('slug')).last()
        ctx['blog_list'] = Blog.objects.all()
        return ctx


class ContactView(TemplateView):
    template_name = 'static/contact.html'