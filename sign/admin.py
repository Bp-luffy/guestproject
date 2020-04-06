from django.contrib import admin
from sign.models.createTables import Event,Guest

# Register your models here.
class EventAdmin(admin.ModelAdmin):
    list_display = ['event_id','name','status','address','start_time']

class GuestAdmin(admin.ModelAdmin):
    list_display = ['realname','phone','email','sign','create_time','event_id']

admin.site.register(Event,EventAdmin)
admin.site.register(Guest,GuestAdmin)
