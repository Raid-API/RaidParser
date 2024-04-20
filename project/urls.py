from django.contrib import admin
from django.urls import include, path, re_path
from apps.v1.views import index


urlpatterns = [
    re_path(r'^api/', include('api.urls')),
    path('admin/', admin.site.urls),
    path('', index, name='index'),
]
