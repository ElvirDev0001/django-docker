from django.urls import path
from . import views

urlpatterns = [
    path("", views.profile, name="home"),
    path("todos/", views.todos, name="Todos"),
    path('shader-background/', views.shader_background_view, name='shader_background'),
]
