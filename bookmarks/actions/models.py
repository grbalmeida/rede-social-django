from django.db import models

class Action(models.Model):
    # O usuário que executou a ação; é uma ForeignKey para o modelo User de Django
    user = models.ForeignKey('auth.User', related_name='actions', db_index=True, on_delete=models.CASCADE)
    
    # o verbo que descreve a ação realizada pelo usuário
    verb = models.CharField(max_length=255)
    
    created = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        ordering = ('-created',)