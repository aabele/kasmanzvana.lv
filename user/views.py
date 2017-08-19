"""
Application views
"""
from allauth.account import views as auth_views
from django.utils.decorators import method_decorator
from user.decorators import persist_session_vars
from django.views.generic import DetailView
from user import models

from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import DetailView, UpdateView

from user import forms
from website import mixins


@method_decorator(persist_session_vars(['_ask']), name='dispatch')
class LoginView(auth_views.LoginView):
    pass


class UserDetailView(DetailView):
    """
    User public profile view
    """
    model = models.User
    template_name = 'user/details.html'

    def get_object(self, queryset=None):
        self.kwargs[self.pk_url_kwarg] = self.model.get_pk_from_hashid(self.kwargs.get(self.pk_url_kwarg))
        return super().get_object(queryset=None)


class EmailFillView(mixins.LoginRequiredMixin, UpdateView):
    template_name = 'user/email.html'
    model = models.User
    form_class = forms.EmailForm
    success_info = 'Paldies - jūsu epasts ir saglabāts!'

    def get_success_url(self):
        if self.request.GET.get('next'):
            return self.request.GET.get('next')

        return reverse_lazy('website:front')

    def get_object(self, queryset=None):
        return self.model.objects.get(username=self.request.user.username)

    def form_valid(self, form):
        """
        Default actions + save profile fields too
        :param form:
        :return:
        """
        messages.info(self.request, self.success_info)
        return super().form_valid(form)
