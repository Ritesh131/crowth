from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views import View
from django.core.mail import send_mail
from crowth.settings import *
from home_app.models import *
from home_app.forms import *

# Create your views here.


class IndexView(TemplateView):
    template_name = 'static/index.html'

    def get_context_data(self, **kwargs):
        ctx = super(IndexView, self).get_context_data(**kwargs)
        ctx['blog'] = Blog.objects.all()[:3]
        ctx['services'] = Services.objects.all()
        return ctx


class LoaderView(TemplateView):
    template_name = 'static/loader.html'


class BlogView(TemplateView):
    template_name = 'static/blog.html'

    def get_context_data(self, **kwargs):
        ctx = super(BlogView, self).get_context_data(**kwargs)
        ctx['blog'] = Blog.objects.filter(slug=kwargs.get('slug')).last()
        ctx['blog_list'] = Blog.objects.all()
        return ctx


class ContactView(TemplateView):
    template_name = 'static/contact.html'


class ThankView(TemplateView):
    template_name = 'static/thank.html'


class QuerySubmit(View):
    template_name = 'static/thank.html'

    def post(self, request):
        name = request.POST.get('name', None)
        email = request.POST.get('email', None)
        phone = request.POST.get('phone', None)
        message = request.POST.get('message', None)
        print(request.POST.get)
        query_form = QueryForm(data=request.POST)
        if query_form.is_valid():
            query_form.save()
        return render(request, self.template_name)

        query = Query.objects.create(name=name, email=email, phone=phone, message=message)
        try:
            notice = mailer(name, email, phone, message)
            print(notice)
        except Exception as e:
            print('mail not sent', e)
            pass
        return render(request, self.template_name)     

def mailer(name, email, phone, message):
    subject = 'Crowth'
    message = f'{name} just submit a enquiry. \n \t {message}'
    email_from = EMAIL_HOST_USER
    recipient_list = ['bajpairitesh878@gmail.com', ]
    send_mail( subject, message, email_from, recipient_list )