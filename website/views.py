"""
Application views
"""
from django.utils import timezone
from django.views.generic import TemplateView
from phone import models

from django.contrib import messages
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView

from website import forms
from website.models import Message, Visitor

user_model = get_user_model()


class FrontPageView(TemplateView):
    """
    Front page
    """
    template_name = 'website/front.html'

    def get_context_data(self, **kwargs):

        today = timezone.now().date()
        this_month_comments = (models.Comment.objects
                               .filter(insert_date__year=today.year, insert_date__month=today.month)
                               .exclude(author__isnull=True, legacy=True))

        data = super().get_context_data(**kwargs)
        data['last_15_users'] = user_model.objects.exclude(is_staff=True).order_by('-id')[:15]
        data['total_registered_count'] = user_model.objects.exclude(is_staff=True).count()
        data['this_month_registered'] = (user_model.objects
                                         .filter(date_joined__year=today.year, date_joined__month=today.month)
                                         .exclude(legacy=True)
                                         .count())
        data['this_month_comments'] = this_month_comments.count()
        data['this_month_numbers'] = (models.Phone.objects
                                      .filter(pk__in=this_month_comments.values_list('phone_id', flat=True))
                                      .count())
        data['last_comment'] = models.Comment.objects.exclude(author__isnull=True).last()
        return data


class ContactView(CreateView):
    """
    Contact page
    """
    template_name = 'website/write-us.html'
    model = Message
    form_class = forms.ContactForm

    def get_success_url(self):
        return str(reverse('website:contacts')) + '?action=ok'


class SubscribeToNewsView(CreateView):
    """
    Allow users to leave email for news
    """
    model = Visitor
    fields = ['email']
    success_url = reverse_lazy('website:front')
    template_name = 'website/blank.html'

    def form_valid(self, form):
        """
        Form submission extra actions
        :param form: form instance
        :return:
        """
        messages.info(self.request, 'You have been subscribed successfully!')
        return super().form_valid(form)
