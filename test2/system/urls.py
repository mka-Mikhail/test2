from django.urls import path
from system import views

urlpatterns = [
    path('tasks/', views.TaskList.as_view()),
    path('tasks/<int:pk>/', views.TaskRetrieve.as_view()),
    path('tasks/update/<int:pk>/', views.TaskUpdate.as_view()),
    path('tasks/delete/<int:pk>/', views.TaskDestroy.as_view()),
    path('tasks/create/', views.TaskCreate.as_view()),
]
