from django.urls import path
from django.contrib import admin

from . import views

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]