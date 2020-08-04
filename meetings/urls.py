from django.urls import path

from . import views

urlpatterns = [
    path('<int:id>', views.detail, name='detail'),
    path('rooms', views.rooms, name='rooms'),
    path('new', views.new, name='new'),
    path('add_room', views.add_room, name='add_room')
]