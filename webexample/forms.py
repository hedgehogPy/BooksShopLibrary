from django import forms
from .models import Author,Genre,Book
from django.core.exceptions import ValidationError
from re import match
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User



class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['first_name','second_name','info','photo']

        widgets = {
        'first_name': forms.TextInput(attrs={'class':'form-control'}),
        'second_name': forms.TextInput(attrs={'class':'form-control'}),
        'info': forms.TextInput(attrs={'class':'form-control'}),
        'photo': forms.TextInput(attrs={'class':'form-control'}),
        }

    def clean_first_name(self):
        new_first_name = self.cleaned_data['first_name']
        l1 = len(new_first_name)
        pattern = r'^[A-Z][a-z]+'
        res = match(pattern, new_first_name)
        if res is None or l1!=res.span()[1]:
            raise ValidationError('First name can’t contain numbers and symbols and must begin with capital leller')
        return new_first_name

    def clean_second_name(self):
        new_second_name = self.cleaned_data['second_name']
        l1 = len(new_second_name)
        pattern = r'^[A-Z][a-z]+'
        res = match(pattern, new_second_name)
        if res is None or l1!=res.span()[1]:
            raise ValidationError('Second name can’t contain numbers and symbols and must begin with capital letter')
        return new_second_name

class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ['name','info','photo']

        widgets = {
        'name': forms.TextInput(attrs={'class':'form-control'}),
        'info': forms.TextInput(attrs={'class':'form-control'}),
        'photo': forms.TextInput(attrs={'class':'form-control'}),
        }

    def clean_name(self):
        new_name = self.cleaned_data['name']
        genres = Genre.objects.filter(name = new_name)
        print(str(type(self)))
        l1 = len(new_name)
        pattern = r'^[A-Z][a-z]+'
        res = match(pattern, new_name)
        if res is None or l1!=res.span()[1]:
            raise ValidationError('Name can’t contain numbers and symbols and should begin with capital letter')
        if genres.count() > 0 :
           raise ValidationError('Genre with the same name already exist')
        return new_name

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['name','info','price','recomAge','author','genres','photo']

        widgets = {
        'name': forms.TextInput(attrs={'class': 'form-control'}),
        'info': forms.TextInput(attrs={'class': 'form-control'}),
        'price': forms.TextInput(attrs={'class': 'form-control'}),
        'recomAge': forms.TextInput(attrs={'class': 'form-control'}),
        'author': forms.SelectMultiple(attrs={'class': 'form-control'}),
        'genres': forms.SelectMultiple(attrs={'class': 'form-control'}),
        'photo': forms.TextInput(attrs={'class':'form-control'}),
        }

    def clean_price(self):
        new_price = self.cleaned_data['price']
        if new_price < 1 or new_price > 10000:
            raise ValidationError('Price should be bigget than zero and less than ten thousands')
        return new_price

    def clean_recomAge(self):
        new_recomAge = self.cleaned_data['recomAge']
        if new_recomAge < 6 or new_recomAge > 18:
            raise ValidationError('Recomended age should be between 6 and 18')
        return new_recomAge

    def clean_name(self):
        new_name = self.cleaned_data['name']
        pattern = r'^[A-Z][a-z]+'
        res = match(pattern, new_name)
        if res is None:
            raise ValidationError('Name can’t contain numbers and symbols and must begin with capital leller')
        return new_name
