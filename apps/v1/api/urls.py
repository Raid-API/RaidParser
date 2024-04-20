from django.urls import path
from apps.v1.views import parse_website_view


# /api/v1/...

urlpatterns = [
    path('parse-website/', parse_website_view, name='parse_website'),
]
