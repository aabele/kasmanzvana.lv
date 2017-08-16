"""
Application views
"""
from django.views.generic import TemplateView
from phone import models


class FrontPageView(TemplateView):
    """
    Front page
    """
    template_name = 'website/front.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['latest_comments'] = models.Comment.objects.filter(author__isnull=False).order_by('-id')[:5]
        return data
