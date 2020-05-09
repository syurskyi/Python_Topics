c_ DisableCSRF(object):
    ___  -   get_response):
        get_response _ get_response
        # One-time configuration and initialization.

    ___ __call__  request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        setattr(request, '_dont_enforce_csrf_checks', True)
        response _ get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        r_ response
