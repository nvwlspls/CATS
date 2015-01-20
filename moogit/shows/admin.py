from django.contrib import admin
from shows.models import Venue, Band, showOrder, show, contact


# Register your models here.
admin.site.register(Venue)
admin.site.register(Band)
admin.site.register(showOrder)
admin.site.register(show)
admin.site.register(contact)