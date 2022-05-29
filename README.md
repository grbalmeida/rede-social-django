### Comando para executar o servidor de desenvolvimento com HTTPS

```
python manage.py runserver_plus --cert-file cert.crt
```

### Certifi

Para usar a urllib a fim de obter imagens a partir de URLs servidos via HTTPS,
precisamos instalar o pacote Python Certifi. O Certifi é um conjunto de certificados-raiz
para validar se os certificados SSL/TLS são confiáveis.

### Url Django and Duke

https://127.0.0.1:8000/images/create/?title=%20Django%20and%20Duke&url=https://marodrom.org/content/images/dukedjangopiano-1.jpg