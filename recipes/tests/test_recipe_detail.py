from django.urls import resolve, reverse
from recipes import views

from .test_recipe_base import RecipeTestBase


class RecipeViewsDetailTest(RecipeTestBase):
    def test_recipe_detail_view_function_is_correct(self):
        view = resolve(
            reverse('recipes-recipe', kwargs={'id': 1})
        )
        self.assertIs(view.func, views.recipe)

    def test_recipe_detail_view_returns_404_if_no_recipes_found(self):
        response = self.client.get(
            reverse('recipes-recipe', kwargs={'id': 1000})
        )
        self.assertEqual(response.status_code, 404)

    def test_recipe_detail_loads_template_the_correct_recipes(self):
        # Need a recipe for this test
        title_detail = 'this detail page and load one recipe'
        self.make_recipe(title=title_detail)

        response = self.client.get(reverse('recipes-recipe',
                                           kwargs={
                                               'id': 1
                                           }))
        content = response.content.decode('utf-8')

        # Check if one recipe exists
        self.assertIn(title_detail, content)

    def test_recipe_detail_template_do_load_recipe_not_published(self):
        """Test recipe is_published False dont show"""
        # Need a recipe for this test
        recipe = self.make_recipe(is_published=False)

        response = self.client.get(
            reverse('recipes-recipe', kwargs={'id': recipe.id})
        )

        self.assertEqual(response.status_code, 404)
