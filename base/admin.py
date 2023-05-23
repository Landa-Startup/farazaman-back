from django.contrib import admin
from .models import Startup, Contact, StartupSubmit, Event

admin.site.register(Startup)
admin.site.register(Contact)
admin.site.register(StartupSubmit)
admin.site.register(Event)