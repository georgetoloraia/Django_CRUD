from django.urls import path
from . import views


urlpatterns = [
    path('index', views.index, name="index"),
    # path('todos/', views.TodoList.as_view(), name='todo_list'),
    # path('todos/create/', views.TodoCreate.as_view(), name='todo_create'),
    # path('todos/<int:id>/', views.TodoDetail.as_view(), name='todo_detail'),
    # path('todos/<int:id>/update/', views.TodoUpdate.as_view(), name='todo_update'),
    # path('todos/<int:id>/delete/', views.TodoDelete.as_view(), name='todo_delete'),

    path('todos/get_all_todos/', views.get_all_todos, name='get_all_todos'),
    path('todos/get_todo', views.get_todo, name='get_todo'),
    path('todos/create_todo/', views.create_todo, name='create_todo'),
    path('todos/<int:id>/update_todo/', views.update_todo, name='update_todo'),
    path('todos/<int:id>/delete_todo/', views.delete_todo, name='delete_todo'),
]