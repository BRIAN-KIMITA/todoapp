from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('update_task/<int:pk>',views.updatetask,name='update_task'),
    path('delete_task/<int:pk>',views.deletetask,name='delete_task'),



]


