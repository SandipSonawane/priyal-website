from django.urls import path

from portfolio import views as index_app_views

urlpatterns = [
    path('', index_app_views.index, name='index'),
]
