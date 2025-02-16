from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('index2/<int:val1>/', views.index2),
    path('index/<int:val1>/', views.index),
    path('<int:bookId>', views.viewbook),
]
