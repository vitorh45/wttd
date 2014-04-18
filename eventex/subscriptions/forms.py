#coding: utf-8
from django import forms
from django.utils.translation import ugettext as _

class SubscriptionForm(forms.Form):
	name = forms.CharField(label=_('Nome'))
	email = forms.EmailField(label=_('Email'))
	cpf = forms.CharField(label=_('CPF'))
	phone = forms.CharField(label=_('Telefone'))