from django.http import HttpResponseBadRequest

# Implemente decoradores personalizados para as suas views se perceber
# que está repetindo as mesmas verificações em várias views.

def ajax_required(f):
    def wrap(request, *args, **kwargs):
        # Verifica se o header HTTP_X_REQUEST_WITH é AJAX
        if not request.is_ajax():
            return HttpResponseBadRequest()
        return f(request, *args, **kwargs)
    wrap.__doc__=f.__doc__
    wrap.__name__=f.__name__
    return wrap