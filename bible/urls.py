from django.urls import path
from . import views

urlpatterns = [
    path('', views.bible, name='bible'),
    path('book/<str:book_name>/', views.bible, name='bible_book'),
    path('book/<str:book_name>/chapter/<int:chapter_number>/', views.bible, name='bible_chapter'),
]