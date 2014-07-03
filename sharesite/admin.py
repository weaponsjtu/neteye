from django.contrib import admin
from wangji.sharesite.models import Poll, Choice, Onesite, Comments

class ChoiceInline(admin.TabularInline):
	model = Choice
	extra = 3

class PollAdmin(admin.ModelAdmin):
	list_display = ('question','pub_date')
	list_filter = ['pub_date']
	search_fields = ['question']
	date_hierarchy = 'pub_date'
	fieldsets = [
		('Question',{'fields': ['question'],'classes':['collapse']}),
		('Date information',{'fields':['pub_date'],'classes':['collapse']}),
	]
	inlines = [ChoiceInline]

class CommentsInline(admin.TabularInline):
	model = Comments
	extra = 1

class OnesiteAdmin(admin.ModelAdmin):
	list_display = ('title','logo','domain','value','info','skill','pub_date')
	list_filter = ['pub_date']
	search_fields = ['title']
	fieldsets = [
		('Title',{'fields': ['title']}),
		('Logo',{'fields': ['logo']}),
		('Domain',{'fields':['domain']}),
		('Value',{'fields': ['value']}),
		('Info',{'fields':['info']}),
		('Skill',{'fields': ['skill']}),
		('Date information',{'fields':['pub_date']}),
		#('Domain',{'fields':['domain'],'classes':['collapse']}),
	]
	inlines = [CommentsInline]

admin.site.register(Poll,PollAdmin)
admin.site.register(Onesite,OnesiteAdmin)
