from django import forms
from django.forms import ModelForm, Textarea, TextInput, HiddenInput
from django.contrib.auth.models import User
from .models import Licenciatarios


current_id = Licenciatarios.objects.latest('folio')
next_id = int(current_id.folio) + 1


def add_css_classes(f, **kwargs):
    field - f.formfield(**kwargs)
    if field and 'class' not in field.widget.attrs:
        field.widget.attrs['class'] = 'form-control'
    return field



class AddLicenciatario(ModelForm):
    formafield_callback = add_css_classes
    """docstring for AddLicenciatario."""
    class Meta:
        model = Licenciatarios
        exclude = []
        labels = {
            'folio':'FOLIO'
        }
        help_texts = {
            'folio':'El folio debe ser de seis digitos'
        }
        widgets = {
            'folio': TextInput(attrs={
                'class':'form-control',
                'placeholder':'0001',
                'value' : next_id,
                'autofocus':''
            }),
            'actividad':Textarea(attrs={
                'class':'form-control',
            }),
            'horario': Textarea(attrs={
                'class':'form-control',
            }),
            'nombre': TextInput(attrs={
                'class':'form-control',
            }),
            'razon_social': TextInput(attrs={
                'class':'form-control',
            }),
            'nombre_comercial': TextInput(attrs={
                'class':'form-control',
            }),
            'domicilio': TextInput(attrs={
                'class':'form-control',
            }),
            'colonia': TextInput(attrs={
                'class':'form-control',
            }),
            'municipio': TextInput(attrs={
                'class':'form-control',
            }),
            'entidad': TextInput(attrs={
                'class':'form-control',
            }),
            'cp': TextInput(attrs={
                'class':'form-control',
            }),
            'telefono': TextInput(attrs={
                'class':'form-control',
            }),
            'correo': TextInput(attrs={
                'class':'form-control',
            }),
            'rfc': TextInput(attrs={
                'class':'form-control',
            }),
            'expedicion_fecha': TextInput(attrs={
                'class':'form-control',
            }),
            'vencimiento_fecha': TextInput(attrs={
                'class':'form-control',
            }),
            'latlng': HiddenInput()
        }
        #
    # nombre = forms.CharField(label='Nombre del licenciatario', max_length=200)
    # # apellido = forms.CharField(label='Apellido', max_length=300)
