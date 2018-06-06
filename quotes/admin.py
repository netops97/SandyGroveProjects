from django.contrib import admin
from .models import Quote

class QuoteAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'company', 'submitted', 'quotedate', 'quoteprice')
    list_filter = ('submitted', 'quotedate')
    readonly_fields = ('submitted',)
    fieldsets = (
        (None, {
            'fields': ('name', 'email', 'description')
        }),
        ('Contact Information', {
            'classes': ('collapse',),
            'fields': ('position', 'company', 'address', 'phone', 'web')
        }),
        ('Job Information', {
            'classes': ('collapse',),
            'fields': ('sitestatus', 'priority', 'jobfile', 'submitted')
        }),
        ('Quote Admin', {
            'classes': ('collapse',),
            'fields': ('quotedate', 'quoteprice', 'username')
        }),
    )

admin.site.register(Quote, QuoteAdmin)

# Register your models here.
