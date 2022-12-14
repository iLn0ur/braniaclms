__all__ = ['NewsView']
from django.views.generic import TemplateView

from mainapp.models import News


class NewsView(TemplateView):
    template_name = "mainapp/news/news.html"

    def get_context_data(self, **kwargs):
        # Get all previous data
        context = super().get_context_data(**kwargs)
        # Create your own data
        context["news_qs"] = News.objects.all()[:5]
        return context
