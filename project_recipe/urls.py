from django.urls import path
from recipe import views

app_name = 'recipe'  # Додаємо імена просторів, щоб уникнути конфліктів імен URL

urlpatterns = [
    path('', views.main, name='main'),  # Головна сторінка з рецептами за 2023 рік
    path('recipe/<int:recipe_id>/', views.recipe_detail, name='recipe_detail'),  # Сторінка з деталями рецепта
    path('categories/', views.category_list, name='category_list'),  # Сторінка зі списком категорій
]
