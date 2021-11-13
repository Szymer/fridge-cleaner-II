from itertools import chain

from django.shortcuts import render
from django.views.generic import FormView
from django.views import View

from fridge_cleaner_app.forms import SelectIngridientForm
from fridge_cleaner_app.models import Recipe




def search_recipes(form):
    choises = form.cleaned_data["name"]
    for i in range (15):
        choises_next = form.cleaned_data[f"name{1}"]
        choises = list(chain(choises, choises_next))
    recipes = Recipe.objects.filter(ingredients__in=choises)

    resoult = choises[0].recipe_set.all()
    for ing_name in choises:
        recipse_using_ing_name = ing_name.recipe_set.all()
        resoult = set(recipse_using_ing_name) & set(resoult)

    if not resoult :
        resoult = recipes


    return resoult



class SelectIngridientView(FormView):
    template_name = 'fridge_cleaner_app/home.html'
    form_class = SelectIngridientForm


    def form_valid(self, form):
        recipes = search_recipes(form)

        context = {
            'recipes' : recipes
        }
        return render(self.request, 'fridge_cleaner_app/serch_resoult.html', context )



class RecipeDeatilView(View):
    def get(self, request, recipe_pk, *args, **kwargs):
        # spider = RecpiDeatailsspider
        recipe = Recipe.objects.get(pk=int(recipe_pk))

        context = {"mesage": 'NO data',
                    "url" : recipe.url,
                    "ings": recipe.ingredients.all()
                   }
        return render(request, 'fridge_cleaner_app/detailview.html', context)
