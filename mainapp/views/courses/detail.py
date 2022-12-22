__all__ = ['CoursesDetailView']
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView
from mainapp.forms import CourseFeedbackForm
from mainapp.models import Courses, Lesson, CourseTeachers, CourseFeedback
import logging
from django.conf import settings


logger = logging.getLogger(__name__)


class CoursesDetailView(TemplateView):
    template_name = "mainapp/courses/courses_detail.html"

    logger.debug("debug informer")
    def get_context_data(self, pk=None, **kwargs):
        context = super(CoursesDetailView, self).get_context_data(**kwargs)
        context["course_object"] = get_object_or_404(
            Courses, pk=pk
        )
        context["lessons"] = Lesson.objects.filter(
            course=context["course_object"]
        )
        context["teachers"] = CourseTeachers.objects.filter(
            course=context["course_object"]
        )
        if not self.request.user.is_anonymous:
            if not CourseFeedback.objects.filter(
                    course=context["course_object"], user=self.request.user
            ).count():
                context["feedback_form"] = CourseFeedbackForm(
                    course=context["course_object"], user=self.request.user
                )
        context["feedback_list"] = CourseFeedback.objects.filter(
            course=context["course_object"]
        ).order_by("-created", "-rating")[:5]
        return context
