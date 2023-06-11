from django.contrib import admin
from .models import Startup, Contact, StartupSubmit, Event, Hire, EventAttendees, WorkSpace

admin.site.register(Startup)
admin.site.register(Contact)
admin.site.register(StartupSubmit)
admin.site.register(Hire)
admin.site.register(EventAttendees)
admin.site.register(WorkSpace)


class EventAttendeesInline(admin.TabularInline):
    model = EventAttendees
    extra = 0
    readonly_fields = ('name', 'email', 'phone')
    fields = ('name', 'email', 'phone')
    show_change_link = True

class EventAdmin(admin.ModelAdmin):
    inlines = [EventAttendeesInline]

admin.site.register(Event, EventAdmin)
