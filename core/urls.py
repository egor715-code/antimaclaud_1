from django.urls import path
from . import views

urlpatterns = [
    path('team/<int:team_id>/delete/', views.delete_team, name='delete_team'),
    # Добавьте другие маршруты, если они есть
] 