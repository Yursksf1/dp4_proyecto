from django.contrib import admin
from django.utils.html import format_html

from .models import Certificado
# Register your models here.

class CerficadoAdmin(admin.ModelAdmin):
    list_display = ["nombre", "numero_documento", "get_certificado"]
    search_fields = ["nombre", "numero_documento"]
    list_filter = ["fecha_salida", ]

    @admin.display(empty_value='???')
    def get_certificado(self, obj):
        return format_html('<a href="/media/{}.pdf"> ver certificado </a>'.format(obj.numero_documento))


admin.site.register(Certificado, CerficadoAdmin)

