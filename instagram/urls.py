from django.contrib import admin
from django.conf.urls import url
from django.urls import path
from instagram import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'^IdealWeight/',views.IdealWeight)
]