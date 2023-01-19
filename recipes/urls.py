from django.contrib import admin
from django.urls import path, include
from recipes.views import home, pag_temp

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('temp/', pag_temp)
]
