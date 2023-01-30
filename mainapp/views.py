from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView


# Create your views here.

class ContactView(TemplateView):
    template_name = 'mainapp/contact.html'


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


























# class HelloWorldView(View):
#
#     def get(self, request, *args, **kwargs):
#         return HttpResponse('hello, world!')


# def hello_world(request):
#    return HttpResponse("hello")


# def blog(request):
#     return HttpResponse("i'm blog")
