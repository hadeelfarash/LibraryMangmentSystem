from django import forms
from .models import *


class CategoryForm(forms.ModelForm):
    class Meta:
        model=Category
        # fields='__all__' # ولكن بهذه الطريقة لا يظهر الفورم بشكل مرتب لذلك سنستخدم طريقة ال widgets
        fields=[
            'name',
        ]
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),

            
        }


class BookForm(forms.ModelForm):
    class Meta:
        model=Book
        # fields='__all__' # ولكن بهذه الطريقة لا يظهر الفورم بشكل مرتب لذلك سنستخدم طريقة ال widgets
        fields=[
            'title',
            'author',
            'photo_book',
            'photo_author',
            'pages',
            'rental_price_day',
            'rental_period',
            'total_rental',
            'status',
            'category',
        ]
        widgets={
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'author':forms.TextInput(attrs={'class':'form-control'}),
            'photo_book':forms.FileInput(attrs={'class':'form-control'}),
            'photo_author':forms.FileInput(attrs={'class':'form-control'}),
            'pages':forms.NumberInput(attrs={'class':'form-control'}),
            'rental_price_day':forms.NumberInput(attrs={'class':'form-control','id':'rentalprice'}),
            'rental_period':forms.NumberInput(attrs={'class':'form-control','id':'rentaldays'}),
            # 'active':forms.TextInput(attrs={'class':'form-control'}),
            'status':forms.Select(attrs={'class':'form-control'}),
            'category':forms.Select(attrs={'class':'form-control'}),
            'total_rental':forms.NumberInput(attrs={'class':'form-control','id':'totalrental'}),
            
        }
