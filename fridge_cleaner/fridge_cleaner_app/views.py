from django.shortcuts import render
from django.views.generic import FormView

from fridge_cleaner_app.forms import SelectIngridientForm


class SelectIngridientView(FormView):
    template_name = 'fridge_cleaner_app/home.html'
    form_class = SelectIngridientForm
    # success_url = '/thanks/'