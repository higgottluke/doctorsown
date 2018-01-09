from django.contrib import admin

from cms.extensions import PageExtensionAdmin

from .models import ParametersExtension


class ParametersExtensionAdmin(PageExtensionAdmin):
    pass

admin.site.register(ParametersExtension, ParametersExtensionAdmin)
