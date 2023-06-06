from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from account.models import User


INPUT_CLASSES = 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'
class LoginForm(AuthenticationForm):
    class Meta:
        model = User

    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your username',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your password',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2','tip')

        # widgets = {
        #     'username': forms.TextInput(attrs={
        #         'class': INPUT_CLASSES
        #     }),
        #     'email': forms.TextInput(attrs={
        #         'class': INPUT_CLASSES
        #     }),
        #     'password1': forms.PasswordInput(attrs={
        #         'class': 'w-full py-4 px-6 rounded-xl'
        #     }),
        #     'password2': forms.PasswordInput(attrs={
        #     'placeholder': 'Your password',
        #     'class': 'w-full py-4 px-6 rounded-xl'
        #     }),
        #     'tip': forms.Select(choices=[("K", "Klijent"), ("F", "Firma")],attrs={
        #         'class': INPUT_CLASSES
        #     }),
        # }
    
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your username',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': 'Your email address',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your password',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Repeat password',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
    
    tip = forms.ChoiceField(choices=[("K", "Klijent"), ("F", "Firma")], widget=forms.Select(attrs={
        'placeholder': 'Repeat password',
        'class': 'w-full py-4 px-6 rounded-xl'
    }), required=True)