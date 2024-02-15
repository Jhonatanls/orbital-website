from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label="Nombre", max_length=100, min_length=3, 
                            widget=forms.TextInput(
                            attrs={'placeholder': "Escribe aquí tu nombre"}))
    
    email = forms.EmailField(label="E-mail", required=True, widget=forms.TextInput(
                            attrs={'placeholder': "ejemplo@correo.com"}))
    service_choices = (
        ('Desarrollo móvil', 'Desarrollo móvil'),
        ('Desarrollo web', 'Desarrollo web'),
        ('Desarrollo científico', 'Desarrollo científico'),
        ('Otro', 'Otro')
    )
    service = forms.ChoiceField(label="Servicio que necesita", choices=service_choices, widget=forms.TextInput(
                            attrs={'placeholder': "Selecciona una opción"}))
    description = forms.CharField(label= "Describe en algunas palabras, la solución que necesitas, datos como si es para un negocio o para ti, en cuanto tiempo requieres la solución y si necesitas más asesoría para terminar de darle forma a tu idea y mucho más.",
                                required=True, widget=forms.Textarea(attrs={'row':5, 'cols':20, 'placeholder': "Describe lo que necesitas o haznos más preguntas."}))