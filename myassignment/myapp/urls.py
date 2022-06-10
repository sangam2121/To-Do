from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [




    path('',views.home,name= 'home'),
    path('completed/<int:pk>/',views.completed,name='completed'),
    path('add',views.add, name='add'),
    path('delete/<int:pk>/',views.delete, name='delete'),
    path('deleteall',views.deleteall,name='deleteall'),
    path('edit/<int:pk>/',views.edit, name='edit'),
    #path('update/<int:pk>',views.updatetodo,name='update'),
    path('important/<int:pk>/',views.important, name='important'),
    path('unmark/<int:pk>/',views.unmark, name='unmark'),
   
   
]
