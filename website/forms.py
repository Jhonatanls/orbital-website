from django import forms

class ContactForm(forms.Form):
    name = forms.Charfield(label="Nombre", max_length=100, min_length=3)
    email = forms.EmailField(required=True)
    service_choices = (
        ('Desarrollo móvil', 'Desarrollo móvil'),
        ('Desarrollo web', 'Desarrollo web'),
        ('Desarrollo científico', 'Desarrollo científico'),
        ('Otro', 'Otro')
    )
    service = forms.Charfield(label="Servicio que necesita", choices=service_choices)
    description = forms.Textarea(required=true)