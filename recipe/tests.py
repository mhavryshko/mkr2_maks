from django.test import TestCase
from django.contrib import admin
from .admin import RecipeAdmin, CategoryAdmin
from .models import Recipe, Category


class AdminTestCase(TestCase):
    def test_recipe_admin(self):
        self.assertTrue(admin.site.is_registered(Recipe))
        self.assertIsInstance(admin.site._registry[Recipe], RecipeAdmin)
        self.assertIn('title', RecipeAdmin.list_display)
        self.assertIn('category', RecipeAdmin.list_display)
        self.assertIn('created_at', RecipeAdmin.list_display)
        self.assertIn('updated_at', RecipeAdmin.list_display)
        self.assertIn('category', RecipeAdmin.list_filter)
        self.assertIn('title', RecipeAdmin.search_fields)
        self.assertIn('description', RecipeAdmin.search_fields)
        self.assertIn('created_at', RecipeAdmin.readonly_fields)
        self.assertIn('updated_at', RecipeAdmin.readonly_fields)

    def test_category_admin(self):
        self.assertTrue(admin.site.is_registered(Category))
        self.assertIsInstance(admin.site._registry[Category], CategoryAdmin)
        self.assertIn('name', CategoryAdmin.list_display)
