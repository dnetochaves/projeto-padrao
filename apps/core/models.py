from django.db import models

# Create your models here.
class Confirguracoes(models.Model):
    nome_projeto = models.CharField(max_length=50)
    logo = models.ImageField(upload_to='core_media', height_field=None, width_field=None, max_length=None, null=True, blank=True)

    def listar_configuracoes():
        return Confirguracoes.objects.all()

    def __str__(self):
        return self.nome_projeto
    
