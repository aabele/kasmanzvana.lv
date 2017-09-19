"""
Application model API viewsets
"""

from rest_framework import viewsets, authentication, permissions, mixins, decorators

from phone import models
from phone import serializers


class PhoneViewSet(mixins.ListModelMixin,
                   mixins.RetrieveModelMixin,
                   viewsets.GenericViewSet):
    """
    Viewset for phone.models.Phone
    """
    model = models.Phone
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    queryset = model.objects.all()
    serializer_class = serializers.PhoneSerializer

    def get_object(self):
        """
        Find object by its phone number
        :return: phone object
        """
        obj, _ = self.model.objects.get_or_create(phone=self.kwargs.get('pk'))
        return obj

    @decorators.detail_route(methods=['POST'])
    def vote_plus(self, *args, **kwargs):
        """
        User vote that this number is ok to take
        :return: string
        """
        obj = self.get_object()
        obj.vote_plus(self.request.user)
        return self.retrieve(*args, **kwargs)

    @decorators.detail_route(methods=['POST'])
    def vote_minus(self, *args, **kwargs):
        """
        User vote that this number is NOT ok to take
        :return: string
        """
        obj = self.get_object()
        obj.vote_minus(self.request.user)
        return self.retrieve(*args, **kwargs)

    @decorators.detail_route(methods=['POST'])
    def vote_minus(self, *args, **kwargs):
        """
        User vote that this number is NOT ok to take
        :return: string
        """
        obj = self.get_object()
        obj.vote_minus(self.request.user)
        return self.retrieve(*args, **kwargs)

    @decorators.detail_route(methods=['POST'])
    def follow(self, *args, **kwargs):
        """
        User will follow the news from this object
        :return: string
        """
        obj = self.get_object()
        obj.follow(self.request.user)
        return self.retrieve(*args, **kwargs)

    @decorators.detail_route(methods=['POST'])
    def unfollow(self, *args, **kwargs):
        """
        User will unfollow the news from this object
        :return: string
        """
        obj = self.get_object()
        obj.unfollow(self.request.user)
        return self.retrieve(*args, **kwargs)


class CommentViewSet(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    Viewset for phone.models.Comment
    """
    model = models.Comment
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    queryset = model.objects.all()
    serializer_class = serializers.CommentSerializer
    lookup_field = 'pk'

    def get_object(self):
        pk = self.model.get_pk_from_hashid(self.kwargs.get(self.lookup_field))
        return self.model.objects.get(pk=pk)

    @decorators.detail_route(methods=['POST'])
    def vote_plus(self, *args, **kwargs):
        """
        User vote that this number is ok to take
        :return: string
        """
        obj = self.get_object()
        obj.vote_plus(self.request.user)
        return self.retrieve(*args, **kwargs)

    @decorators.detail_route(methods=['POST'])
    def vote_minus(self, *args, **kwargs):
        """
        User vote that this number is NOT ok to take
        :return: string
        """
        obj = self.get_object()
        obj.vote_minus(self.request.user)
        return self.retrieve(*args, **kwargs)
