from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)

    def __str__(self):
        return f'Profile for user {self.user.username}'

# Se precisar de campos adicionais em um relacionamento de muitos
# para muitos, crie um modelo personalizado com uma ForeignKey para
# cada lado do relacionamento. Acrescente um ManyToManyField em um dos
# modelos relacionados e diga ao Django que seu modelo intermediário
# deve ser usado incluindo-o no parâmetro through
class Contact(models.Model):
    # Uma ForeignKey para o usuário que cria o relacionamento
    user_from = models.ForeignKey('auth.User', related_name='rel_from_set', on_delete=models.CASCADE)

    # Uma ForeignKey para o usuário que está sendo seguido
    user_to = models.ForeignKey('auth.User', related_name='rel_to_set', on_delete=models.CASCADE)
    
    created = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return f'{self.user_from} follows {self.user_to}'

# Adiciona o campo following dinamicamente em User
user_model = get_user_model()
user_model.add_to_class('following',
                        models.ManyToManyField('self',
                                                through=Contact,
                                                related_name='followers',
                                                symmetrical=False))

# Ao usar um modelo intermediário para relacionamentos de muitos
# para muitos, alguns dos métodos do gerenciador relacionado estarão
# desativados, por exemplo, add(), create() ou remove(). Em vez disso, você
# terá de criar ou remover instâncias do modelo intermediário.