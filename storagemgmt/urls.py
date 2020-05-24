from django.urls import path
from . import views
from filebrowser.sites import site

urlpatterns = [
    path('', views.nav, name='nav'),
    path('filebrowser/', site.urls),
]