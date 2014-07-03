from django.contrib import admin
from pinax.apps.account.models import Account
from django.contrib.auth.models import User
from wangji.people.models import MessageBoard

class MessageBoardInline(admin.TabularInline):
	model = MessageBoard
	extra = 1

class UserAdmin(admin.ModelAdmin):
	inlines = [CommentsInline]

admin.site.register(User, UserAdmin)
admin.site.register(Account)

