from django.urls import path

from movie.views import (
     create_movie_view,
     detail_movie_view,
     edit_movie_view,
     add_sale_movie
)

app_name = "movie"

urlpatterns = [
    path('create/', create_movie_view, name = 'create'),
    path('<slug>/', detail_movie_view, name = 'detail'),
    path('<slug>/edit', edit_movie_view, name = 'edit'),
    path('add-sale-movie/<slug>/', add_sale_movie, name='add-sale'),
]

