from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='books.index'),  # Home page
    path('list_books/', views.list_books, name='books.list_books'),  # List Books page
    path('aboutus/', views.aboutus, name='books.aboutus'),  # About Us page
    path('<int:bookId>/', views.viewbook, name='books.view_one_book'),  # View a specific book
    path('html5/links/', views.links_page, name='links_page'),
    path('html5/text/formatting/', views.text_formatting_view, name='formatting_page'),
    path('html5/listing/', views.listing_page, name='listing_page'),
    path('html5/tables/', views.tables_page, name='tables_page'),
    path('search/', views.search_books, name='search_books'),
]
