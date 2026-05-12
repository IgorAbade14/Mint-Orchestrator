# Importações necessárias para a aplicação
import os  # Para acessar variáveis de ambiente
import socket  # Para obter informações da máquina (hostname)
from flask import Flask  # Framework web para criar a API

# Inicializa a aplicação Flask
app = Flask(__name__)

@app.get("/")
def home():
    # Obtém o nome do pod/container (hostname do sistema)
    pod_name = socket.gethostname()
    
    # Obtém o nome do nó do cluster via variável de ambiente
    node_name = os.getenv("NODE_NAME", "Minikube Cluster")
    
    # HTML com CSS imbuído para um visual "Dark Mode" de DevOps
    return f"""
    <!DOCTYPE html>
    <html lang="pt-br">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Mint-Orchestrator</title>
        <style>
            /* Estilos gerais do corpo da página */
            body {{
                background-color: #0d1117;
                color: #c9d1d9;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
            }}
            
            /* Container principal (cartão) */
            .card {{
                background-color: #161b22;
                border: 1px solid #30363d;
                border-radius: 12px;
                padding: 40px;
                box-shadow: 0 8px 24px rgba(0,0,0,0.5);
                text-align: center;
                max-width: 500px;
            }}
            
            /* Título principal */
            h1 {{
                color: #238636;
                margin-bottom: 10px;
            }}
            
            /* Container com informações do Pod */
            .pod-info {{
                background-color: #010409;
                padding: 15px;
                border-radius: 6px;
                font-family: 'Courier New', Courier, monospace;
                color: #79c0ff;
                margin-top: 20px;
                border-left: 4px solid #238636;
            }}
            
            /* Indicador de status (ponto verde) */
            .status {{
                display: inline-block;
                width: 12px;
                height: 12px;
                background-color: #238636;
                border-radius: 50%;
                margin-right: 8px;
            }}
        </style>
    </head>
    <body>
        <div class="card">
            <h1>🌿 Mint-Orchestrator v1.0</h1>
            <p>Infraestrutura orquestrada com sucesso!</p>
            <!-- Card exibindo dados do pod e do nó do cluster -->
            <div class="pod-info">
                <span class="status"></span>
                <strong>Pod ID:</strong> {pod_name}<br>
                <small>Ambiente: {node_name}</small>
            </div>
        </div>
    </body>
    </html>
    """

# Ponto de entrada da aplicação
if __name__ == "__main__":
    # Inicia o servidor Flask escutando em todas as interfaces (0.0.0.0) na porta 5000
    app.run(host="0.0.0.0", port=5000)