from django import forms


class UserNameForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        label='Ваше имя',
        widget=forms.TextInput(attrs={'placeholder': 'Введите ваше имя'}),
        error_messages={'required': 'Пожалуйста, введите имя.'},
    )
