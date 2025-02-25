from django.shortcuts import render, get_object_or_404
from django.utils.timezone import datetime
from .models import Recipe
from .models import Category


def main(request):
    year = 2023
    recipes = Recipe.objects.filter(created_at__year=year)
    return render(request, 'main.html', {'recipes': recipes})

def recipe_detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    return render(request, 'recipe_detail.html', {'recipe': recipe})

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'category_list.html', {'categories': categories})
