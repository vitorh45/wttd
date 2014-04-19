from django.contrib import admin
from django.utils.timezone import now
from django.utils.translation import ugettext as _
from eventex.subscriptions.models import Subscription

class SubscriptionAdmin(admin.ModelAdmin):
	list_display = ['name','email','cpf','phone','created_at','subscribed_today', 'paid']
	date_hierarchy = 'created_at'
	search_field = ('name','email','cpf','phone','created_at')
	list_filter = ['created_at', 'paid']

	def subscribed_today(self, obj):
		return obj.created_at.date() == now().date()
	subscribed_today.short_description = _('Inscrito hoje?')
	subscribed_today.boolean = True

admin.site.register(Subscription, SubscriptionAdmin)