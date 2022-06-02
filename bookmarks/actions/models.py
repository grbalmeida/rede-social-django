from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

class Action(models.Model):
    # O usuário que executou a ação; é uma ForeignKey para o modelo User de Django
    user = models.ForeignKey('auth.User', related_name='actions', db_index=True, on_delete=models.CASCADE)
    
    # o verbo que descreve a ação realizada pelo usuário
    verb = models.CharField(max_length=255)
    
    # Um campo ForeignKey para ContentType: informará o modelo para o relacionamento
    target_ct = models.ForeignKey(ContentType,
                                  blank=True,
                                  null=True,
                                  related_name='target_obj',
                                  on_delete=models.CASCADE)

    # Um campo para armazenar a chave primária do objeto relacionado: em
    # geral, será um PositiveIntegerField para que esteja de acordo com os campos
    # automáticos de chave primária de Django
    target_id = models.PositiveIntegerField(null=True,
                                            blank=True,
                                            db_index=True)

    # Um campo para definir e gerenciar o relacionamento genérico usando os
    # dois campos anteriores: o framework contenttypes disponibiliza um campo
    # GenericForeignKey para isso.
    target = GenericForeignKey('target_ct', 'target_id')

    created = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        ordering = ('-created',)