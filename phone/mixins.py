from django.conf import settings
from hashids import Hashids


class HashidMixin(object):

    hashids = Hashids(salt=settings.HASHID_FIELD_SALT)

    def get_hashid_pk(self):
        """
        Get object pk encoded as hashid string
        :return: string
        """
        return str(self.hashids.encode(self.pk))

    @classmethod
    def get_pk_from_hashid(cls, hash):
        """
        Get object primary key from hashids hashes
        :param hash:
        :return:
        """
        try:
            return int(cls.hashids.decode(hash)[0])
        except IndexError:
            return None
