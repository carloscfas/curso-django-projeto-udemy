from django.test import TestCase
from django.urls import reverse

class RecipeURLsTest(TestCase):
    def test_the_pytest_is_ok(self):
        ...

    def test_recipe_home_url_is_correct(self):
        home_url = reverse('recipes:home')
        self.assertEqual(home_url, '/')

    def test_recipe_category_url_is_correct(self):
        url_category = reverse('recipes:category', kwargs={'category_id': 1})
        self.assertEqual(url_category, '/recipes/category/1/')

    def test_recipe_detail_url_is_correct(self):
        url_recipe = reverse('recipes:recipe', kwargs={'id': 1})
        self.assertEqual(url_recipe, '/recipes/1/')
