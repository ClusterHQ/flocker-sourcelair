from django.shortcuts import redirect


class HttpRedirectMiddleware(object):
    """
    Middleware used for demo, in order to make sure HTTP only is used and thus
    the WebSocket works.l
    """

    def process_request(self, request):
        """
        Redirect to HTTP URL, if HTTPS is supplied. WebSockets will not work
        over non-secure protocol and the server does not support it for the
        time being.
        """
        path = request.path.lstrip('/')
        if request.is_secure():
            host = request.get_host()
            return redirect('http://%s%s' % (host, request.get_full_path()))
