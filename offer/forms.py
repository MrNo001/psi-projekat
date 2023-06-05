from django import forms
from .models import Offer, Picture

INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border'

"""
class NewOfferForm(forms.ModelForm):
    class Meta:
        model = Offer
        fields = ('name','model','description', 'price','godiste','body', 'images')
        widgets = {
            
            'name': forms.TextInput(attrs={
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
            'godiste':forms.NumberInput(attrs={
                'class':INPUT_CLASSES
            }),
            'body': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
            'images': forms.FileInput(attrs = {
                'class': INPUT_CLASSES,
            }),
        }
"""

"""
class NewPictureForm(forms.ModelForm):
    class Meta:
        model=Picture
        fields = ('image')
        widgets = {  
            'image': forms.ImageField(attrs={
                'class': INPUT_CLASSES
            })
        }
"""

class EditOfferForm(forms.ModelForm):
   class Meta:
        model = Offer
        fields = ('name', 'model', 'description', 'price', 'year', 'body_type')
        widgets = {
            
            'name': forms.TextInput(attrs={
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
                'class':INPUT_CLASSES
            }),
            'body_type': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
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


class NewOfferForm(forms.Form):

    name = forms.CharField(max_length=255)
    description = forms.Textarea()

    make = forms.CharField(max_length=255)
    model = forms.CharField(max_length=255)
    year = forms.IntegerField()
    mileage = forms.IntegerField()
    body_type = forms.ChoiceField(choices=Offer.BODY_TYPES)
    fuel_type = forms.ChoiceField(choices=Offer.FUEL_TYPES)
    gearbox = forms.ChoiceField(choices=Offer.GEARBOX_TYPES)
    power = forms.IntegerField()

    price = forms.FloatField()

    file_field = MultipleFileField()


