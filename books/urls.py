from django.urls import path
from .views import BookList,book_list

urlpatterns = [
    path('BookList/',BookList.as_view(),name='BookList'),
    path('Book_List/',book_list,name='Book_List'),
]