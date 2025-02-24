from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='books.index'),  # Home page
    path('list_books/', views.list_books, name='books.list_books'),  # List Books page
    path('aboutus/', views.aboutus, name='books.aboutus'),  # About Us page
    path('<int:bookId>/', views.viewbook, name='books.view_one_book'),  # View a specific book
]
