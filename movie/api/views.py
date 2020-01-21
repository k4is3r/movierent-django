from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authentication import TokenAuthentication
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter, OrderingFilter


from account.models import Account
from movie.models import MoviesRent, UpdateLog
from movie.api.serializers import MovieRentSerializer
from copy import deepcopy


@api_view(['GET', ])
#@authentication_classes((TokenAuthentication,))
#@permission_classes((IsAuthenticated,))
def api_detail_movie_view(request, slug):
    
    try:
        movie_list = MoviesRent.objects.get(slug=slug)

    except MoviesRent.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        serializers = MovieRentSerializer(movie_list)
        return Response(serializers.data)


@api_view(['PUT', ])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def api_update_movie_view(request, slug):
    
    try:
        movie_list = MoviesRent.objects.get(slug=slug)

    except MoviesRent.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    user = request.user

    if movie_list.owner != user:
        return Response({'response':'You dont have permission to edit'})
    
    old_movie = deepcopy(movie_list)

    if request.method == 'PUT':
        serializers = MovieRentSerializer(movie_list,data=request.data)
        data = {}
        if serializers.is_valid():
            serializers.save()
            update_log = UpdateLog()
            update_log.title = old_movie.title
            update_log.old_rentail_price = old_movie.rentail_price
            update_log.old_sale_price = old_movie.sale_price
            update_log.save()
            data['success'] = 'update succesful'
            return Response(data=data)
        return Response(serializers.errors, status= status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE', ])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def api_delete_movie_view(request, slug):
    
    try:
        movie_list = MoviesRent.objects.get(slug=slug)

    except MoviesRent.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
   
    user = request.user

    if movie_list.owner != user:
        return Response({'response':'You dont have permission to delete this movie'})
 
    if request.method == "DELETE":
        operation = movie_list.delete()
        data = {}
        if operation:
            data['success'] = "delete successful"
        else:
            data['failure'] = "delete fail"
        return Response(data=data)


@api_view(['POST', ])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,IsAdminUser))
def api_create_movie_view(request):
    
    account = request.user
    
    movie = MoviesRent(owner=account)
    
    if request.method == "POST":
        serializer = MovieRentSerializer(movie, data=request.data)
       
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ApiMovieListView(ListAPIView):
    queryset = MoviesRent.objects.all()
    serializer_class = MovieRentSerializer
    pagination_class = PageNumberPagination
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('title','description')
 
