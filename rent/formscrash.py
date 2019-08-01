from django import forms

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from rent.models import Pool, Booking


class CreatePoolForm(forms.ModelForm):
    class Meta:
        model = Pool
        fields = ['title', 'description', 'address', 'capacity', 'price', 'length', 'width', 'type', 'heated', 'image']


class CreateBookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['date', 'participants']


class RegistrationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name = cleaned_data['first_name']
        user.last_name = cleaned_data['last_name']
        user.email = cleaned_data['email']

        if commit:
            user.save()

        return user


class ConnexionForm(forms.Form):
    username = forms.CharField(label="Nom d'utilisateur", max_length=30)
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)