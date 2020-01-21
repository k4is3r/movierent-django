from rest_framework import serializers
from movie.models import MoviesRent


class MovieRentSerializer(serializers.ModelSerializer):

    username = serializers.SerializerMethodField('get_username_from_owner')

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
                  'username'
                  ]


    def get_username_from_owner(self, movie):
        username = movie.owner.username
        return username
