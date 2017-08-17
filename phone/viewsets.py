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
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    queryset = models.Phone.objects.all()
    serializer_class = serializers.PhoneSerializer
    lookup_field = 'phone'

    @decorators.detail_route(methods=['POST'])
    def vote_plus(self, *args, **kwargs):
        """
        User vote that this number is ok to take
        :return: string
        """
        phone = self.get_object()
        phone.vote_plus(self.request.user)
        return response.Response('Voted')

    @decorators.detail_route(methods=['POST'])
    def vote_minus(self, *args, **kwargs):
        """
        User vote that this number is NOT ok to take
        :return: string
        """
        phone = self.get_object()
        phone.vote_minus(self.request.user)
        return response.Response('Voted')
