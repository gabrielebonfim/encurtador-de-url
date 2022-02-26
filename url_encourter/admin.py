from django.contrib import admin

from url_encourter.models import Url


class UrlAdmin(admin.ModelAdmin):
    list_display= ('url', 'token', 'ativo')
    exclude = ('token', 'ativo',)


admin.site.register(Url, UrlAdmin)
