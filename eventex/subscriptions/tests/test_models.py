#coding: utf-8
from django.test import TestCase
from django.db import IntegrityError
from datetime import datetime
from eventex.subscriptions.models import Subscription

class SubscriptionTest(TestCase):
	def setUp(self):
		self.obj = Subscription(
			name='Vitor Hugo Campos',
			cpf='12345678901',
			email='vitorh45@gmail.com',
			phone='19-99350909'
		)
	def test_create(self):
		'Subscription must exists'
		self.obj.save()
		self.assertEqual(1, self.obj.pk)

	def test_has_created_at(self):
		'subscription must have automatic created_at'
		self.obj.save()
		self.assertIsInstance(self.obj.created_at, datetime)

	def test_unicode(self):
		self.assertEqual(u'Vitor Hugo Campos', unicode(self.obj))

	def test_paid_default_value_is_False(self):
		'By default paid must be False.'
		self.assertEqual(False, self.obj.paid)

class SubscriptionUniqueTest(TestCase):
	def setUp(self):
		# Create a first entry to force the collision
		Subscription.objects.create(name='Vitor Hugo Campos', cpf='12345678901',
		email='vitorh45@gmail.com', phone='19-99350909')

	def test_cpf_unique(self):
		'CPF must be unique'
		s = Subscription(name='Vitor Hugo Campos', cpf='12345678901',
		email='vitor@gmail.com', phone='19-99350909')
		self.assertRaises(IntegrityError, s.save)

	def test_email_unique(self):
		'Email must be unique'
		s = Subscription(name='Vitor Hugo Campos', cpf='00000000011',
		email='vitorh45@gmail.com', phone='19-99350909')
		self.assertRaises(IntegrityError, s.save)



	