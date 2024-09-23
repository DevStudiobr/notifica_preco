import requests
from bs4 import BeautifulSoup
import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Função para buscar o preço do produto
def obter_preco_produto(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Pegando o preço do produto (isso varia de site para site)
    preco = soup.find('span', {'class': 'price-tag'}).get_text()
    return float(preco.replace('R$', '').replace(',', '').strip())

# Função para enviar e-mail de notificação
def enviar_email(preco_atual, preco_desejado, email_destino):
    # Informações do servidor de e-mail (usando Gmail como exemplo)
    remetente = "seuemail@gmail.com"
    senha = "suasenha"
    
    # Configurações do e-mail
    msg = MIMEMultipart()
    msg['From'] = remetente
    msg['To'] = email_destino
    msg['Subject'] = "Alerta de Preço: O produto atingiu o valor desejado!"
    body = f"O produto que você está monitorando caiu para R${preco_atual}. O valor desejado era R${preco_desejado}."
    msg.attach(MIMEText(body, 'plain'))

    # Enviar e-mail via SMTP
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(remetente, senha)
    text = msg.as_string()
    server.sendmail(remetente, email_destino, text)
    server.quit()

# URL do produto e preço desejado
url_produto = 'https://www.exemplo.com/produto'
preco_desejado = 150.00  # Exemplo de preço desejado

# Endereço de e-mail do usuário
email_usuario = 'emailusuario@example.com'

# Loop de monitoramento
while True:
    preco_atual = obter_preco_produto(url_produto)
    
    print(f"Preço atual: R${preco_atual}")
    
    # Verifica se o preço atual é menor ou igual ao preço desejado
    if preco_atual <= preco_desejado:
        enviar_email(preco_atual, preco_desejado, email_usuario)
        print("Notificação enviada por e-mail!")
        break
    
    # Espera 1 hora antes de verificar novamente
    time.sleep(3600)
