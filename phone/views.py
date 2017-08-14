"""
Application views
"""
from django.views.generic import DetailView, CreateView

from phone import forms
from phone import models


class PhoneDetailView(DetailView):
    """
    Phone profile page
    """
    model = models.Phone
    comment_form = forms.CommentForm
    template_name = 'phone/phone.html'

    def get(self, *args, **kwargs):
        return super().get(*args, **kwargs)

    def get_object(self):
        try:
            self.model.objects.get(phone=self.kwargs.get('number'))
        except self.model.DoesNotExist:
            return {}

    def get_number(self):
        """
        Get existing number or non existing from the kwargs
        :return: string
        """
        try:
            return self.object.phone
        except AttributeError:
            return self.kwargs.get('number')

    def get_context_data(self, **kwargs):
        data = super().get_context_data()
        data['number'] = self.get_number()
        data['form'] = self.comment_form()
        return data


class CommentCreateView(CreateView):
    """
    Create comment
    """
    model = models.Comment
    form_class = forms.CommentForm

    def form_valid(self, form):
        user = self.request.user
        session = self.request.session

        if user.is_authenticated():
            form.instance.author = user
        else:
            if not session.session_key:
                session.create()
            form.instance.anonymous_session = session.session_key

        super().form_valid(form)

    def get_success_url(self):
        return self.object.phone.get_absolute_url()
