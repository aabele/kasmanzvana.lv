"""
Application views
"""
from allauth.account import views as auth_views
from django.utils.decorators import method_decorator
from user.decorators import persist_session_vars
from django.views.generic import DetailView
from user import models


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
