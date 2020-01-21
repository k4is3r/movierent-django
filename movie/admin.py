
from django.contrib import admin

from movie.models import MoviesRent, UpdateLog, UserSaleHistory


admin.site.register(MoviesRent)
admin.site.register(UpdateLog)
admin.site.register(UserSaleHistory)
