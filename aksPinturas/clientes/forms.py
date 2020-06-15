from django import forms

from .models import clientes

class clientesForm(forms.ModelForm):
    class Meta:        
        model = clientes
        is_company = forms.BooleanField(required=False)
        is_employee = forms.BooleanField(required=False)
        is_supplier = forms.BooleanField(required=False)
        profile_image = forms.ImageField()

        
        fields = [
            'profile_image',
            'name',
            'surname',
            'phone',
            'country',
            'is_company',
            'is_employee',
            'is_supplier',
        ]
        labels = {
            'profile_image': 'Perfil',
            'name' : 'Nombre',
            'surname' : 'Apellidos',
            'phone' : 'Telefono',
            'country': 'Pais',
            'is_company': 'Es Empresa',
            'is_employee': 'Es Empleado',
            'is_supplier': 'Es Proveedor',
        }
        widgets = {  
            'name': forms.TextInput(attrs={'class':'form-control'}), 
            'surname': forms.TextInput(attrs={'class':'form-control'}),  
            'phone' : forms.TextInput(attrs={'class':'form-control'}), 
            'country': forms.Select(attrs={'class':'form-control'}),
            'is_company': forms.CheckboxInput(attrs={'class':'form-control'}),
            'is_employee': forms.CheckboxInput(attrs={'class':'form-control'}),
            'is_supplier': forms.CheckboxInput(attrs={'class':'form-control'}),
        }