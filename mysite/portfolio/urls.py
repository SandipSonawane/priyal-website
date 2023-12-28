from django.urls import path

from portfolio import views as index_app_views

urlpatterns = [
    path('', index_app_views.index, name='index'),
    path('snake', index_app_views.snake, name='snake'),
    path('flashcard', index_app_views.flashcard, name='flashcard'),
]
