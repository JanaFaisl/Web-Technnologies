from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,  name='books.index'),  # Home page
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
    path('lab9_part1/listbooks', views.list_books, name='books.list_books'),
    path('lab9_part1/addbook', views.add_book, name='books.add_book'),
    path('lab9_part1/editbook/<int:id>', views.edit_book, name='books.edit_book'),
    path('lab9_part1/deletebook/<int:id>', views.delete_book, name='books.delete_book'),

      # Part 2
    path('lab9_part2/listbooks', views.list_books, name='books.list_books_form'),
    path('lab9_part2/addbook', views.add_book_form, name='books.add_book_form'),
    path('lab9_part2/editbook/<int:id>', views.edit_book_form, name='books.edit_book_form'),
    path('lab9_part2/deletebook/<int:id>', views.delete_book, name='books.delete_book_form'),

    path('html5/t/', views.t, name='t'),

    path('list/', views.student_list, name='student_list'),
    path('add/', views.add_student, name='add_student'),
    path('update/<int:pk>/', views.update_student, name='update_student'),
    path('delete/<int:pk>/', views.delete_student, name='delete_student'),

    path('list2/', views.student2_list, name='student2_list'),
    path('add-student2/', views.add_student2, name='add_student2'),
    path('update-student2/<int:pk>/', views.update_student2, name='update_student2'),

    path('add-product/', views.add_product, name='add_product'),
    path('products/', views.product_list, name='product_list'),


]
