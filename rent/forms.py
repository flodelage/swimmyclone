from django import forms

from rent.models import Pool

class CreatePoolForm(forms.ModelForm):
    class Meta:
        model = Pool
        fields = ['title', 'description', 'address', 'capacity', 'price', 'length', 'width', 'type', 'heated', 'image']
