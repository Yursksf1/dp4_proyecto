from django.db import models

# Create your models here.

class Certificado(models.Model):
    nombre = models.CharField(max_length=100)
    tipo_documento = models.CharField(max_length=5)
    numero_documento = models.CharField(max_length=20)
    email = models.EmailField()
    fecha_salida = models.DateField()
    ruta_del_certificado = models.CharField(max_length=500, default="")

    def __str__(self):
        return '{} - {}'.format(self.nombre, self.numero_documento)

    def get_pdf(self):
        return "media/{}.pdf".format(self.numero_documento)