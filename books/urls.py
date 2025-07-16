from django.urls import path
from .views import BookList,book_list

urlpatterns = [
    path('BookList/',BookList.as_view(),name='BookList'),
    path('book_list/',book_list,name='book_list'),
]