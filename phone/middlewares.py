"""
Application middlewares
"""


class AnonymousIDMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        if not request.user.is_authenticated():
            if not request.session.session_key:
                request.session.create()
            request.session['_ask'] = request.session.session_key

        response = self.get_response(request)

        return response
