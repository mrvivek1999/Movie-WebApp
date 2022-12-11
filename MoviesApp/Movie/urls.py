

from xml.dom.minidom import Document
from .views import *


from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', index, name= 'index'),
    path('add_Movies/', add_Movies, name='add_movies'),
    path('movie/search/', search_movies, name='search'),
    path('view_movie/<int:movie_id>/', view_movie  , name='view_movie'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
