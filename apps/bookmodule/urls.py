from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='books.index'),  # Home page
    path('list_books/', views.list_books, name='books.list_books'),  # List Books page
    path('simple/query/', views.simple_query, name='books.simple_query'), 
    path('complex/query/', views.complex_query, name='books.complex_query'), 
    path('aboutus/', views.aboutus, name='books.aboutus'),  # About Us page
    path('<int:bookId>/', views.viewbook, name='books.view_one_book'),  # View a specific book
    path('html5/links/', views.links_page, name='links_page'),
    path('html5/text/formatting/', views.text_formatting_view, name='formatting_page'),
    path('html5/listing/', views.listing_page, name='listing_page'),
    path('html5/tables/', views.tables_page, name='tables_page'),
    path('search/', views.search_books, name='search_books'),
    path('lab8/task1/', views.lab8_task1, name='books.lab8_task1'), 
    path('lab8/task2/', views.lab8_task2, name='books.lab8_task2'), 
    path('lab8/task3/', views.lab8_task3, name='books.lab8_task3'), 
    path('lab8/task4/', views.lab8_task4, name='books.lab8_task4'), 
    path('lab8/task5/', views.lab8_task5, name='books.lab8_task5'), 
    path('lab8/task7/', views.lab8_task7, name='books.lab8_task7'),
    path('lab9/task1', views.task1, name='books.lab9_task1'),
    path('lab9/task2', views.task2, name='books.lab9_task2'),
    path('lab9/task3', views.task3, name='books.lab9_task3'),
    path('lab9/task4', views.task4, name='books.lab9_task4'),
]
