from rest_framework import serializers
from movie.models import MoviesRent


class MovieRentSerializer(serializers.ModelSerializer):
  class Meta:
      model = MoviesRent
      fields = ['title',
                'description',
                'image',
                'likes',
                'stock',
                'rentail_price',
                'sale_price',
                'date_published',
                ]
