from django.contrib import admin
from eventex.subscriptions.models import Subscription

class SubscriptionAdmin(admin.ModelAdmin):
	pass

admin.site.register(Subscription, SubscriptionAdmin)