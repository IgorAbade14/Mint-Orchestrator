FROM python:3.9-slim

# Definimos o diretório de trabalho antes de copiar
WORKDIR /app

# Copiamos o conteúdo da pasta 'app' local para a pasta '/app' no container
# Usamos a barra no final (/app/) para o Docker entender que é um diretório
COPY ./app /app/

# Instalamos as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Expomos a porta que o Flask usa
EXPOSE 5000

# Comando para rodar a aplicação usando Gunicorn    
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app.main:app", "--workers", "3"]