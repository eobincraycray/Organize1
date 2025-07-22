from django import forms
from django.contrib.auth.models import User

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

    email = forms.EmailField(
        required=True,  # Garante que o email seja obrigatório
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'})
    )
