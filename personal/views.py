from django.shortcuts import render
from operator import attrgetter
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from movie.models import MoviesRent
from movie.views import get_movie_queryset

MOVIE_PER_PAGE = 4

def home_screen_view(request):
    headers = request.headers
    content = {}
    
    query = ""
    if request.GET:
        query = request.GET.get('q', '')
        content['query'] = str(query)    

    movie_list = sorted(get_movie_queryset(query), key=attrgetter('date_published'), reverse=True)
    
    
    #pagination
    page = request.GET.get('page', 1)
    movie_list_paginator = Paginator(movie_list, MOVIE_PER_PAGE)
    try:
        movie_list = movie_list_paginator.page(page)
    except PageNotAnInteger:
        movie_list = movie_list_paginator.page(MOVIE_PER_PAGE)
    except EmptyPage:
        movie_list = movie_list_paginator.page(movie_list_paginator.num_pages)

    content['movie_list'] =  movie_list
    
    return render(request, "personal/home.html",content)
