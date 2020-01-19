from django.shortcuts import render, redirect, get_object_or_404

from movie.models import MoviesRent
from movie.forms import CreateMovieForm, UpdateMovieForm
from account.models import Account


def create_movie_view(request):
    content = {}
    
    user = request.user
    
    if not user.is_authenticated:
        return redirect('must_authenticate')

    form = CreateMovieForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        obj = form.save(commit=False)
        owner = Account.objects.filter(email=user.email).first()
        obj.owner = owner
        obj.save()
        form = CreateMovieForm()

    content['form'] = form
 
    return render(request, "movie/create_movie.html", content)

def detail_movie_view(request, slug):
    content = {}
    
    movie = get_object_or_404(MoviesRent, slug=slug)
    content['movie'] = movie
    
    return render(request, 'movie/detail_movie.html', content)


def edit_movie_view(request, slug):
    content = {}
    
    user = request.user
    if not user.is_authenticated:
        return redirect("must_authenticate")

    movie = get_object_or_404(MoviesRent, slug=slug)
    if request.POST:
        form = UpdateMovieForm(request.POST or None, request.FILES or None, instance=movie)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            content['success_message'] = "Updated"
            movie = obj
    form = UpdateMovieForm(
           initial ={
                   "title": movie.title,
                   "description": movie.description,
                   "image": movie.image,
                   "stock": movie.stock,
                   "rentail_price": movie.rentail_price,
                   "sale_price": movie.sale_price,
                   "avility" : movie.avility,
           } 
        )
    content['form'] = form
    return render(request, 'movie/edit_movie.html', content)



