# Especificar la imagen base de Alpine
FROM alpine:latest

# Usar la directiva RUN para instalar curl
RUN apk add --no-cache curl

# Usar la directiva COPY para añadir el archivo config.txt al contenedor
COPY config.txt /app/config.txt

# Comando por defecto para mantener el contenedor en ejecución (opcional)
CMD ["sh"]
