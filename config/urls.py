from django.contrib import admin
from django.urls import path, include
from member.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('polls/', include('polls.urls')),
    path('board/', include('polls.urls')),
    path('', home),
    path('member/', include('member.url')),
]