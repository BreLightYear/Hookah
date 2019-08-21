from django import forms

from .choices import ACCOUNT_TYPE_CHOICES, DISTRICT, TYPE_SEX

from allauth.account.forms import (SignupForm,
                                   LoginForm)
from crispy_forms import (bootstrap,
                          layout)
from crispy_forms.helper import FormHelper

from market.apps.core.models import UserProfile


class MarketLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super(MarketLoginForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)
        self.helper.layout = layout.Layout(
            layout.Fieldset(
                '',
                'login',
                'password'
            ),
            bootstrap.FormActions(
                layout.Submit('submit', 'Log in', css_class='btn btn-success'),
            ),
        )


class MarketSignupForm(SignupForm):
    tipo = forms.ChoiceField(choices=ACCOUNT_TYPE_CHOICES)
    name = forms.CharField(max_length=200)
    sexo = forms.ChoiceField(choices=TYPE_SEX, required=True)
    adress = forms.CharField(max_length=50, required=True)
    adress_number = forms.CharField(max_length=16, required=True)
    district = forms.ChoiceField(choices=DISTRICT, required=True)
    
    def __init__(self, *args, **kwargs):
        super(MarketSignupForm,self).__init__(*args, **kwargs)

        # TODO: Add help texts
        self.helper = FormHelper(self)
        self.helper.layout = layout.Layout(
            layout.Fieldset(
                '',
                'tipo',
                'name',
                'sexo',
                'adress',
                'adress_number',
                'district',
                'email',
                'password1',
                'password2',
            ),
            bootstrap.FormActions(
                layout.Submit('submit', 'Create an account', css_class='btn btn-success'),
            ),
        )
