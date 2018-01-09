from django.db import models

from cms.extensions import PageExtension
from cms.extensions.extension_pool import extension_pool

from filer.fields.image import FilerImageField

@extension_pool.register
class ParametersExtension(PageExtension):
    header_image = models.BooleanField(default=False, help_text="Enable header image. If enabled, more placeholders will appear in Structure mode.")



# Custom Context Processor
def custom_context_processor(request):
    _d = {}
    _d['request_context'] = str(dir(request))
    _d['toolbar_context'] = str(dir(request.toolbar))
    _d['toolbar_em'] = str(request.toolbar.edit_mode)
    _d['toolbar_bm'] = str(request.toolbar.build_mode)
    return _d
