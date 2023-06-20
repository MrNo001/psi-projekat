from django import forms
from .models import Offer, Picture

# INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border'
INPUT_CLASSES = 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'


class NewOfferForm(forms.ModelForm):
    class Meta:
        model = Offer
        fields = ('name', 'make', 'model', 'description', 'price', 'year', 'mileage', 'gearbox', 'body_type', 'fuel_type', 'power')
        widgets = {
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'make': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'model': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'description': forms.Textarea(attrs={
                'class': INPUT_CLASSES
            }),
            'price': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'year':forms.NumberInput(attrs={
                'class': INPUT_CLASSES
            }),
            'mileage':forms.NumberInput(attrs={
                'class': INPUT_CLASSES
            }),
            'gearbox': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
            'body_type': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
            'fuel_type': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
            'power': forms.NumberInput(attrs={
                'class': INPUT_CLASSES
            }),
        }
        labels = {
            'name': 'Naslov',
            'make': 'Marka',
            'model': 'Model',
            'description': 'Opis oglasa',
            'price': 'Cena',
            'year': 'Godište',
            'mileage': 'Kilometraža',
            'gearbox': 'Vrsta menjača',
            'body_type': 'Karoserija',
            'fuel_type': 'Vrsta goriva',
            'power': 'Snaga motora (u kW)',
        }


class EditOfferForm(forms.ModelForm):
    class Meta:
        model = Offer
        fields = ('name', 'make', 'model', 'description', 'price', 'year', 'mileage', 'gearbox', 'body_type', 'fuel_type', 'power')
        widgets = {
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'make': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'model': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'description': forms.Textarea(attrs={
                'class': INPUT_CLASSES
            }),
            'price': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'year':forms.NumberInput(attrs={
                'class': INPUT_CLASSES
            }),
            'mileage':forms.NumberInput(attrs={
                'class': INPUT_CLASSES
            }),
            'gearbox': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
            'body_type': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
            'fuel_type': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
            'power': forms.NumberInput(attrs={
                'class': INPUT_CLASSES
            }),
        }
        labels = {
            'name': 'Naslov',
            'make': 'Marka',
            'model': 'Model',
            'description': 'Opis oglasa',
            'price': 'Cena',
            'year': 'Godište',
            'mileage': 'Kilometraža',
            'gearbox': 'Vrsta menjača',
            'body_type': 'Karoserija',
            'fuel_type': 'Vrsta goriva',
            'power': 'Snaga motora (u kW)',
        }


class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True


class MultipleFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = single_file_clean(data, initial)
        return result


class FileFieldForm(forms.Form):

    file_field = MultipleFileField()


# class NewOfferForm(forms.Form):

#     name = forms.CharField(max_length=255)
#     description = forms.Textarea()

#     make = forms.CharField(max_length=255)
#     model = forms.CharField(max_length=255)
#     year = forms.IntegerField()
#     mileage = forms.IntegerField()
#     body_type = forms.ChoiceField(choices=Offer.BODY_TYPES)
#     fuel_type = forms.ChoiceField(choices=Offer.FUEL_TYPES)
#     gearbox = forms.ChoiceField(choices=Offer.GEARBOX_TYPES)
#     power = forms.IntegerField()

#     price = forms.FloatField()

#     file_field = MultipleFileField()
