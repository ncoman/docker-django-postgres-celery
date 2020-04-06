from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

from .views import my_html_view, five_hundred_test
# Swagger
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='API')

urlpatterns = [
    # Production
    path('admin/', admin.site.urls, name='admin'),
    path('client/', include('client.urls')),

    path('swagger/', schema_view, name='swagger'),
    # keep that line to fix 'rest_framework' is not a registered namespace error.
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

if bool(settings.DEBUG):
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    import debug_toolbar

    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),

    ]
urlpatterns += [path('silk/', include('silk.urls', namespace='silk'))]
