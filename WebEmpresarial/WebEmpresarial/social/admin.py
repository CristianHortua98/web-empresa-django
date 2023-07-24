from django.contrib import admin
from .models import Link

class LinkAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

    def get_readonly_fields(self, request, obj=None):
        if request.user.groups.filter(name="Personal").exists():
            return ('key', 'name', 'font_awesome')
        else:
            return ('created', 'updated')


admin.site.register(Link, LinkAdmin)
