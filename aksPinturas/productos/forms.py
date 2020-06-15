from django import forms

from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:        
        model = Product
        product_image = forms.ImageField()

        
        fields = [
            'product_image',
            'name',
            'code',
            'description',
            'list_price',
            'category',
            'quantity',
        ]
        labels = {
            'product_image': 'Foto de Producto',
            'name': 'Nombre',
            'code': 'Codigo del producto',
            'description': 'Descripcion del producto',
            'list_price': 'Precio del producto',
            'category': 'Nombre categoria',
            'quantity': 'cantidad inicial'
        }
        widgets = {  
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'code': forms.TextInput(attrs={'class':'form-control'}),
            'description': forms.TextInput(attrs={'class':'form-control'}),
            'list_price': forms.NumberInput(attrs={'class':'form-control'}),
            'category': forms.Select(attrs={'class':'form-control'}),
            'quantity': forms.NumberInput(attrs={'class':'form-control'}),
        }