from django.contrib import admin
from django.urls import path, include

from app.views import hello_view, index_view, time_view, workdir_view


urlpatterns = [

    path('admin/', admin.site.urls),
    path('', index_view, name='index'),
    path('hi/', hello_view, name='hello'),
    path('time_now/', time_view, name='time'),
    path('pwd_now/', workdir_view, name='pwd'),
]