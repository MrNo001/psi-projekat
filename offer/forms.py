from django import forms
from .models import Offer, Picture

INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border'

class NewOfferForm(forms.ModelForm):
    class Meta:
        model = Offer
        fields = ('name','model','description', 'price','godiste','body')
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
        }

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
        fields = ('name','model','description', 'price','godiste','body')
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
        }