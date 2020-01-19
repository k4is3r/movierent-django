from django import forms
from movie.models import MoviesRent

class CreateMovieForm(forms.ModelForm):
    
    class Meta:
        model = MoviesRent
        fields = ['title',
                  'description',
                  'image',
                  'stock',
                  'rentail_price',
                  'sale_price']


class UpdateMovieForm(forms.ModelForm):
    
    class Meta:
        model = MoviesRent
        fields= ['title',
                 'description',
                 'image',
                 'stock',
                 'rentail_price',
                 'sale_price',
                 'avility'
                ]
    
    def save(self, commit=True):
        movie = self.instance
        movie.title =  self.cleaned_data['title']
        movie.description =  self.cleaned_data['description']
        movie.stock =  self.cleaned_data['stock']
        movie.rentail_price =  self.cleaned_data['rentail_price']
        movie.sale_price =  self.cleaned_data['sale_price']
        movie.avility =  self.cleaned_data['avility']
        
        if self.cleaned_data['image']:
            movie.image = self.cleaned_data['image']

        if commit:
            movie.save()
        return movie
        
