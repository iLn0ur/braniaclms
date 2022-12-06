from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView


# Create your views here.

class ContactView(TemplateView):
    template_name = 'mainapp/contacts.html'


class CoursesListView(TemplateView):
    template_name = 'mainapp/courses_list.html'


class DocSiteView(TemplateView):
    template_name = 'mainapp/doc_site.html'


class IndexView(TemplateView):
    template_name = 'mainapp/index.html'


class LoginView(TemplateView):
    template_name = 'mainapp/login.html'


class NewsView(TemplateView):
    template_name = 'mainapp/news.html'

    def get_context_data(self, **kwargs):
        # Get all previous data
        context = super().get_context_data(**kwargs)
        # Create your own data
        context["news_title"] = "Громкий новостной заголовок"
        context["news_preview"] = "Предварительное описание, которое заинтересует каждого"
        return context

























# class HelloWorldView(View):
#
#     def get(self, request, *args, **kwargs):
#         return HttpResponse('hello, world!')


# def hello_world(request):
#    return HttpResponse("hello")


# def blog(request):
#     return HttpResponse("i'm blog")
