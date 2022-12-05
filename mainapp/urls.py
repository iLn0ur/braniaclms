from django.urls import path
from mainapp import views
from mainapp.apps import MainappConfig


app_name = MainappConfig.name


urlpatterns = [

    path('contacts/', views.ContactView.as_view()),
    path('courses/', views.CoursesListView.as_view()),
    path('docsite/', views.DocSiteView.as_view()),
    path('', views.IndexView.as_view()),
    path('login/', views.LoginView.as_view()),
    path('news/', views.NewsView.as_view()),





    # path('', views.HelloWorldView.as_view()),
    # path('blog/', views.blog),

]
