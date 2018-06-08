from django import forms
from localflavor.us.forms import USStateField, USStateSelect
from .models import Restaurant

class AddRestaurantForm(forms.Form):
    name = forms.CharField()
    address = forms.CharField()
    town = forms.CharField()
    state = USStateField(widget=USStateSelect)


class AddDishForm(forms.Form):
    restaurant = forms.CharField()
    name = forms.CharField()
    price = forms.DecimalField(max_digits=10, decimal_places=2)
    rating = forms.IntegerField(help_text="Please rate 1-5", max_value=5, min_value=1)
    comment = forms.CharField(widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super(AddDishForm, self).__init__(*args, **kwargs)
        self.fields['restaurant'] = forms.ModelChoiceField(queryset=Restaurant.objects.all())