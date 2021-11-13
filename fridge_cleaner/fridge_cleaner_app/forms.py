from django import forms

from fridge_cleaner_app.models import Ingredient, IngredientTyp


class SelectIngridientForm(forms.Form):
    ing_types = IngredientTyp.objects.all()
    name = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple, label=' Bakalie', required=False,  queryset=Ingredient.objects.filter(typ=ing_types[0].pk))
    name1 = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple, label='Czekolada',required=False, queryset=Ingredient.objects.filter(typ=ing_types[1].pk))
    name2 = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple, label='Grzyby',required=False, queryset=Ingredient.objects.filter(typ=ing_types[2].pk))
    name3 = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple, label='Jaja',required=False, queryset=Ingredient.objects.filter(typ=ing_types[3].pk))
    name4 = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple, label='Kasze',required=False, queryset=Ingredient.objects.filter(typ=ing_types[4].pk))
    name5 = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple, label='Makaron',required=False, queryset=Ingredient.objects.filter(typ=ing_types[5].pk))
    name6 = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple, label='',required=False, queryset=Ingredient.objects.filter(typ=ing_types[6].pk))
    name7 = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple, label='Ser',required=False, queryset=Ingredient.objects.filter(typ=ing_types[7].pk))
    name8 = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple, label='Owoce ',required=False, queryset=Ingredient.objects.filter(typ=ing_types[8].pk))
    name9 = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple, label='Owoce morza',required=False, queryset=Ingredient.objects.filter(typ=ing_types[9].pk))
    name10 = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple, label='Roliny eegzotyczne',required=False, queryset=Ingredient.objects.filter(typ=ing_types[10].pk))
    name11 = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple, label='Ryby',required=False, queryset=Ingredient.objects.filter(typ=ing_types[11].pk))
    name12 = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple, label='Ryź',required=False, queryset=Ingredient.objects.filter(typ=ing_types[12].pk))
    name13 = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple, label='Warzywa',required=False, queryset=Ingredient.objects.filter(typ=ing_types[13].pk))

