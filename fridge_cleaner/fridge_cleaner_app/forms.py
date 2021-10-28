from django import forms

from fridge_cleaner_app.models import create_Ingridient_dict


class SelectIngridientForm(forms.Form):
    name = forms.ChoiceField(choices=create_Ingridient_dict(), widget=forms.SelectMultiple)




