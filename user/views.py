"""
Application views
"""
from allauth.account import views as auth_views
from django.utils.decorators import method_decorator
from user.decorators import persist_session_vars


@method_decorator(persist_session_vars(['_ask']), name='dispatch')
class LoginView(auth_views.LoginView):
    pass
