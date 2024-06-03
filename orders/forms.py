import re
from django import forms


class CreateOrderForm(forms.Form):

    first_name = forms.CharField()
    last_name = forms.CharField()
    phone_number = forms.CharField()
    requires_delivery = forms.ChoiceField(
        choices=[
        ('0', 'False'),
        ('1', 'True'),
        ]
    )
    delivery_address = forms.CharField(required=False)
    payment_on_get = forms.ChoiceField(
        choices=[
        ('0', 'False'),
        ('1', 'True'),
        ]
    )


    def clean_phone_number(self):
        data = self.cleaned_data['phone_number']

        if data.strip('0123456789-') != '':
            raise forms.ValidationError('Номер телефона должен содержать только цифры и знак тере')
        
        pattern = re.compile(r'^\d{3}-\d{3}-\d{2}-\d{2}$')
        if not pattern.match(data):
            raise forms.ValidationError('Неверный формат номера')
        
        return data