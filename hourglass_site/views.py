from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


@login_required()
def example_protected_view(request):
    return HttpResponse('<p>You have successfully authenticated</p>')


def oauth_callback(request):
    # python-social-auth would rather use its handler for /complete/uaa
    # which finishes out the flow and fills out stuff in the django models
    # but I have not been able to get that working
    return HttpResponse('<p>Oauth Callback</p>')
