from django.urls import path
from movie.api.views import(
     api_detail_movie_view,
     api_update_movie_view,
     api_delete_movie_view,
     api_create_movie_view,
     ApiMovieListView,
)
app_name = 'movie'

urlpatterns = [
    path('<slug>/', api_detail_movie_view, name='detail'),
    path('<slug>/update', api_update_movie_view, name='update'),
    path('<slug>/delete', api_delete_movie_view, name='delete'),
    path('create', api_create_movie_view, name='create'),
    path('list', ApiMovieListView.as_view(), name='list'),
]


