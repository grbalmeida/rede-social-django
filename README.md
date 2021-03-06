### Comando para executar o servidor de desenvolvimento com HTTPS

```
python manage.py runserver_plus --cert-file cert.crt
```

### Certifi

Para usar a urllib a fim de obter imagens a partir de URLs servidos via HTTPS,
precisamos instalar o pacote Python Certifi. O Certifi é um conjunto de certificados-raiz
para validar se os certificados SSL/TLS são confiáveis.

### Easy-Thumbnails

Estamos exibindo a imagem original na página de detalhes, porém as dimensões
das diferentes imagens podem variar consideravelmente. Além disso, os arquivos
originais de algumas imagens podem ser enormes, e carregá-los poderia demorar
muito. A melhor forma de exibir imagens otimizadas de maneira uniforme é por
meio de miniaturas (thumbnails).

### CSRF em requisições AJAX

Com a proteção contra CSRF ativa, Django verifica se há um token CSRF em todas as requisições POST.
Ao submeter os formulários, podemos usar a tag de template {% csrf_token %} para enviar o token
junto com o formulário. Entretanto, é um pouco inconveniente para as requisições AJAX passarem
o CSRF como um dado de POST a cada requisição POST. Desse modo, Django permite que você
defina um cabeçalho X-CSRFToken personalizado em suas requisições AJAX, contendo o valor
do token CSRF.

### Usando o framework contenttypes

Django inclui um framework contenttypes que está em django.contrib.contenttypes.
Essa aplicação é capaz de monitorar todos os modelos instalados em seu projeto
e oferecer uma interface genérica para interagir com eles.

# Adicionando ações dos usuários no registro de atividades

Armazenaremos uma ação para cada uma das seguintes interações:

- um usuário marcou uma imagem
- um usuário curtiu uma imagem
- um usuário criou uma conta
- um usuário começou a seguir outro usuário

# Otimizando QuerySets que envolvem objetos relacionados

### Usando select_related()

Django disponibiliza um método de QuerySet chamado select_related() que
permite obter os objetos relacionados em relacionamentos de um para muitos.
Isso se traduz para um QuerySet único, mais complexo, porém evita consultas
adicionais ao acessar objetos relacionados. O método select_related serve para campos
ForeignKey e OneToOne. Ele funciona executando uma JOIN SQL e incluindo os campos
do objeto relacionado na instrução SELECT.

Usar select_related() com cuidado pode reduzir bastante o tempo de execução.

### Usando prefetch_related()

O método select_related() ajudará a melhorar o desempenho para obter objetos
relacionados em relacionamentos de um para muitos. No entanto, select_related()
não funciona para relacionamentos de muitos para muitos ou de muitos para um
(campos ManyToMany ou ForeignKey inversos). Django disponibiliza um método diferente
no QuerySet, chamado prefetch_related, que funciona para relacionamentos de muitos
para muitos e de muitos para um, além de relacionamentos aceitos por select_related().

# Usando sinais para desnormalizar contadores

Há alguns casos em que vamos querer desnormalizar nossos dados. A desnormalização
(desnormalization) consiste em deixar dados redundantes de modo a otimizar
o desempenho na leitura. Por exemplo, você poderia copiar dados relacionados
a um objeto a fim de evitar queries de leitura custosas no banco de dados relacionados.
Exemplo: O modelo Image tem likes, é possível criar um contador de likes e
cada vez que for um inserido um registro Action do tipo like, esse contador será atualizado.

### Trabalhando com sinais

- pre_save e post_save são enviados antes ou depois da chamada do método save() de um modelo
- pre_delete e post_delete são enviados antes ou depois da chamado do método delete() de um modelo ou de um QuerySet
- m2m_changed é enviado quando um ManyToManyField em um modelo é alterado

**IMPORTANTE:**

Há várias maneiras de melhorar o desempenho, as quais você deve levar em
consideração antes de desnormalizar campos. Considere os índices do banco
de dados, a otimização de queries e o caching antes de começar a desnormalizar seus dados

**IMPORTANTE:**

Os sinais de Django são síncronos e bloqueantes. Não confunda sinais com tarefas
assíncronas. Entretanto, é possível combiná-los para disparar tarefas assíncronas
quando seu código receber uma notificação por meio de um sinal.

Devemos conectar nossa função receptora a um sinal de modo que ela seja chamada
sempre que o sinal for enviado. O método recomendado para registrar seus sinais
é importá-los no método ready() da classe de configuração de sua aplicação.

### Classes de configuração de aplicações

Para registrar suas funções receptoras de sinais, se você usar o decorador receiver(),
bastará importar o módulo signals de sua aplicação no método ready() da classe de
configuração da aplicação. Esse método será chamado assim que o registro da aplicação
estiver totalmente preenchido.

# Redis

### Usando o Redis com python

Comando para instalação do Redis com Docker:

```
docker run -d --name redis-stack -p 6379:6379 -p 8001:8001 redis/redis-stack:latest
```

### Armazenando visualizações de itens no Redis

Vamos definir uma forma de armazenar o número total de vezes que uma imagem foi
visualizada. Se você implementar isso com o ORM de Django, a solução envolverá
uma query SQL UPDATE sempre que uma imagem for exibida. Se usarmos o Redis,
bastará incrementar um contador armazenado na memória, resultando em um desempenho
muito melhor e em menor overhead.

**IMPORTANTE:**

A convenção para nomear chaves no Redis consiste em utilizar um sinal de dois-pontos
como separador para criar chaves com namespaces. Ao fazer isso, os nomes das chaves
serão particularmente extensos, e chaves relacionadas compartilharão partes do mesmo
esquema em seus nomes.

### Armazenando um ranking no Redis

Vamos implementar algo mais complexo com o Redis. Criaremos um ranking das imagens mais
visualizadas em nossa plataforma. Para implementar esse ranking, usaremos os conjuntos
ordenados do Redis. Um conjunto ordenado é um conjunto de strings sem repetiação, no
qual cada membro é associado a uma pontuação. Os itens são ordenados de acordo com sua pontuação.

### Url Django and Duke

https://127.0.0.1:8000/images/create/?title=%20Django%20and%20Duke&url=https://marodrom.org/content/images/dukedjangopiano-1.jpg