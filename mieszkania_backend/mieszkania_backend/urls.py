from django.contrib import admin
from django.urls import path

from mieszkania.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('apartments', ApartmentGenericAPI.as_view()),
    path('apartments/<int:pk>', ApartmentGenericAPI.as_view()),
]
