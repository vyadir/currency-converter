from django import forms

class CurrencyForm(forms.Form):
    amount = forms.FloatField(
        label="Monto en COP",
        min_value=0.01,
        error_messages={
            'required': 'Por favor ingrese un monto.',
            'min_value': 'El monto debe ser mayor a cero.',
            'invalid': 'Ingrese un número válido (use punto decimal).',
        },
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ej: 10000',
            'aria-label': 'Monto en pesos colombianos',
            'step': 'any',
            'autofocus': 'autofocus',
        })
    )