from django.urls import path
from Tareasapp import views

urlpatterns = [
    path('tasks', views.tareas_api),
    #path('auth/register',views.UsuarioView.as_view(), name='usuarios_list'),
    path('tasks/delete/<id>',views.tareas_api)
]