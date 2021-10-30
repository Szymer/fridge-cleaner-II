from django.shortcuts import render
from django.views.generic import FormView

from fridge_cleaner_app.forms import SelectIngridientForm
from fridge_cleaner_app.models import Recipe




def search_recipes(form):

    recipes = Recipe.objects.filter(ingredient__in=form.cleaned_data["name"]) #zminic name na ingridients
    return recipes



class SelectIngridientView(FormView):
    template_name = 'fridge_cleaner_app/home.html'
    form_class = SelectIngridientForm


    def form_valid(self, form):
        recipes = search_recipes(form)
        context = {
            'recipes' : recipes
        }
        return render(self.request, 'fridge_cleaner_app/serch_resoult.html', context )

