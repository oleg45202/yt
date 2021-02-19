from django.conf import settings
from django.conf.urls import url
from django.urls import path, include
from django.views.static import serve

urlpatterns = [
    path('', include('core.urls')),
    url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT})
]
