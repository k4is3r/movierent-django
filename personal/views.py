from django.shortcuts import render
from operator import attrgetter
from movie.models import MoviesRent

def home_screen_view(request):
    headers = request.headers
    content = {}

    movie_list = sorted(MoviesRent.objects.all(), key=attrgetter('date_published'), reverse=True)
    content['movie_list'] = movie_list
    
    return render(request, "personal/home.html",content)
