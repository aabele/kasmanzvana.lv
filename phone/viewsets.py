"""
Application model API viewsets
"""

from rest_framework import viewsets, authentication, permissions, mixins, decorators, response

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
    lookup_field = 'phone'

    def get_object(self):
        obj, _ = self.model.objects.get_or_create(phone=self.kwargs.get(self.lookup_field))
        return obj

    @decorators.detail_route(methods=['POST'])
    def vote_plus(self, *args, **kwargs):
        """
        User vote that this number is ok to take
        :return: string
        """
        phone = self.get_object()
        phone.vote_plus(self.request.user)
        return self.retrieve(*args, **kwargs)

    @decorators.detail_route(methods=['POST'])
    def vote_minus(self, *args, **kwargs):
        """
        User vote that this number is NOT ok to take
        :return: string
        """
        phone = self.get_object()
        phone.vote_minus(self.request.user)
        return self.retrieve(*args, **kwargs)
