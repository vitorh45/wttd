#coding: utf-8
from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm

class SubscribeTest(TestCase):
	def setUp(self):
		self.resp = self.client.get("/inscricao/")

	def test_get(self):
		'Get /inscricao/ must return status code 200'
		self.assertEqual(200, self.resp.status_code)

	def test_template(self):
		'Response should be a rendered template'
		self.assertTemplateUsed(self.resp, 'subscriptions/subscription_form.html')

	def test_html(self):
		'html must contains input controls'
		self.assertContains(self.resp, '<form')
		self.assertContains(self.resp, '<input', 6)
		self.assertContains(self.resp, 'type="text"', 3)
		self.assertContains(self.resp, 'type="email"')
		self.assertContains(self.resp, 'type="submit"')

	def test_csrf(self):
		'html must contain csrf token'
		self.assertContains(self.resp, 'csrfmiddlewaretoken')

	def test_has_form(self):
		'context must have the subscription form'
		form = self.resp.context['form']
		self.assertIsInstance(form, SubscriptionForm)

	def test_form_has_fields(self):
		'form must have 4 fields'
		form = self.resp.context['form']
		self.assertItemsEqual(['name','email','cpf','phone'], form.fields)


