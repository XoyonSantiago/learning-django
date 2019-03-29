from django.urls import path

from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),  # link del href de post_list para cada post
    path('post/new', views.post_new, name='post_new'),  # para la ruta de crear nuevo post
     path('post/<int:pk>/edit/', views.post_edit, name='post_edit'), # ruta editar los post
]
