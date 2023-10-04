from django.contrib import admin
from django.urls import path
from asosiyApp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index),
    path('', login_view),
    path('logout/', logout_view),
    path('edit/', edit),
]
