from django.contrib import admin
from .models import Router

class RouterAdmin(admin.ModelAdmin):
    list_display = ('hostname',
                    'address',
                    'state',
                    'username',
                    'password',
                    'ticketnumber',
                    'created_at')
    list_filter = ( 'state',
                    'username',
                    'created_at')
    #readonly_fields = ('hostname',)

admin.site.register(Router,RouterAdmin)
