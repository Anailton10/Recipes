from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=66)

    def __str__(self) -> str:
        return self.name


class Recipe(models.Model):
    title = models.CharField(max_length=66)
    description = models.CharField(max_length=166)
    slug = models.SlugField()
    preparation_time = models.IntegerField()
    preparation_time_unit = models.CharField(max_length=66)
    servings = models.IntegerField()
    servings_unit = models.CharField(max_length=66)
    preparation_steps = models.TextField()
    preparation_steps_is_html = models.BooleanField(default=False)
    # Gera uma data no momento da criação
    created_at = models.DateTimeField(auto_now_add=True)
    # Gera uma data de acordo com alteração
    updated_at = models.DateField(auto_now=True)
    is_published = models.BooleanField(default=False)
    cover = models.ImageField(upload_to='recipes/cover/%Y/%m/%d/')
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True
    )
    author = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True
    )

    def __str__(self) -> str:
        return self.title
