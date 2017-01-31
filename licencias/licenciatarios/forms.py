from django import forms

class AddLicenciatario(forms.Form):
    """docstring for AddLicenciatario."""
    nombre = forms.CharField(label='Nombre del licenciatario', max_length=200)
