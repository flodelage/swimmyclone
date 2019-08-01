from django import forms
from django.contrib.auth.models import User
from rent.models import Pool, Booking, Profile


class CreatePoolForm(forms.ModelForm):
    class Meta:
        model = Pool
        fields = ['title', 'description', 'address', 'capacity', 'price', 'length', 'width', 'type', 'heated', 'image']


class CreateBookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['date', 'participants']


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'password', 'email')


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('image',)
