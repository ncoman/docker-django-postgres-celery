# Here is the test views.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello here is test app.")


def five_hundred_test(request):
    raise ValueError("raising this on purpose for testing for 500")
    # return None


def my_html_view(request):
    response_content = """
    <html>
    <head><title>Hello World!</title>
    <body>
        <h1>This is a demo.</h1>
    </body>
    </html>
    """
    return HttpResponse(response_content)
