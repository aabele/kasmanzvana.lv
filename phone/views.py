"""
Application views
"""
from django.contrib import messages
from django.http import Http404
from django.views.generic import DetailView, CreateView, TemplateView

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
            obj = self.model.objects.get(phone=self.kwargs.get('number'))
        except self.model.DoesNotExist:
            obj = {}

        if models.RemovedPhone.objects.filter(phone=self.kwargs.get('number')).exists():
            raise Http404
        else:
            self.object = obj
        return obj

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
        """
        Add additional template context
        :param kwargs:
        :return: data dictionary
        """
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
    template_name = 'phone/comment/create.html'

    def form_valid(self, form):
        user = self.request.user
        session = self.request.session

        if user.is_authenticated():
            form.instance.author = user
        else:
            form.instance.anonymous_session = session.session_key

        return super().form_valid(form)

    def get_success_url(self):
        """
        If user is not authenticated - ask him to do so otherwise the comment will be removed in 7 days
        :return: string
        """
        if self.request.user.is_authenticated():
            messages.info(self.request, 'Tavs komentārs tika pievienots')
            return self.object.phone.get_absolute_url()
        else:
            return self.object.get_absolute_url()


class CommentProfileView(DetailView):
    """
    Ask user to log in before showing his comment
    """
    model = models.Comment
    template_name = 'phone/comment/profile.html'

    def get_object(self, queryset=None):
        self.kwargs[self.pk_url_kwarg] = self.model.get_pk_from_hashid(self.kwargs.get(self.pk_url_kwarg))
        return super().get_object(queryset=None)


class CategoryView(TemplateView):
    """ Display list 00-99 with all numbers """
    template_name = 'phone/category.html'

    def get_namespace_items(self):
        return models.Phone.get_namespace(prefix=self.kwargs.get('category'))

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['namespace'] = self.get_namespace_items()
        return data
