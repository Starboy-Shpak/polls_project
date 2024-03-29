from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls')),
    path('', include('polls.urls')),
    path('auth/', include('django.contrib.auth.urls')),
]
