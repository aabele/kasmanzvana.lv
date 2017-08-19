from django import http
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin

from app.urls import ADMIN_URL


class EmailMiddleware(MiddlewareMixin):
    """
    Require user email...
    """
    def process_request(self, request):
        """
        If authenticated user is trying to access public website without email filled it - it will be redirected to
        the email form.

        :param request: django request
        :return: None or redirect
        """
        if request.user.is_authenticated():
            url = reverse('users:account_fill_email')
            if not (request.path.startswith('/{0}'.format(ADMIN_URL)) or request.path.startswith(url)):
                if request.method == 'GET':
                    if not request.user.email:
                        return http.HttpResponseRedirect('{0}?next={1}'.format(str(url), request.path))
