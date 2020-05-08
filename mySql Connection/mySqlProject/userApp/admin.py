from django.contrib import admin
from userApp.models import Details
# Register your models here.
admin.site.register(Details)

admin.site.site_title='My Login Page'

admin.site.site_header = 'My DJango Page'

admin.site.index_title = 'Index title'