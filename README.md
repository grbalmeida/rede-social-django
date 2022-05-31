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

### Url Django and Duke

https://127.0.0.1:8000/images/create/?title=%20Django%20and%20Duke&url=https://marodrom.org/content/images/dukedjangopiano-1.jpg