from django import forms


from fridge_cleaner_app.models import Ingredient


class SelectIngridientForm(forms.Form):
    name = forms.ModelMultipleChoiceField(queryset=Ingredient.objects.all())




