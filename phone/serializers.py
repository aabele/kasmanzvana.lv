"""
Application model serializers
"""

from rest_framework import serializers

from phone import models


class PhoneSerializer(serializers.ModelSerializer):
    """
    Serializer for phone.models.Phone
    """

    class Meta(object):
        """
        Serializer meta options
        """
        model = models.Phone
        fields = ('pk', 'phone', 'rating_value', 'get_positive_votes', 'get_negative_votes')
