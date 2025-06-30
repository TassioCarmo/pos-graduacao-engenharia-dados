from kafka import KafkaProducer
import json
import time

# Configuração do produtor Kafka
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',  # Endereço do Kafka
    value_serializer=lambda v: json.dumps(v).encode('utf-8')  # Serializa JSON para bytes
)

# Simular envio de transações
transacoes = [
    {"id": 1, "valor": 100.50, "moeda": "EUR"},
    {"id": 2, "valor": 250.00, "moeda": "USD"},
    {"id": 3, "valor": 75.30, "moeda": "BRL"},
    {"id": 4, "valor": 120.75, "moeda": "GBP"},
    {"id": 5, "valor": 330.40, "moeda": "JPY"},
    {"id": 6, "valor": 50.00, "moeda": "CAD"},
    {"id": 7, "valor": 220.10, "moeda": "AUD"},
    {"id": 8, "valor": 15.80, "moeda": "CHF"},
    {"id": 9, "valor": 600.00, "moeda": "INR"},
    {"id": 10, "valor": 400.25, "moeda": "CNY"}
]

for transacao in transacoes:
    print(f"Enviando: {transacao}")
    producer.send('transacoes', transacao)  # Enviar mensagem para o tópico
    time.sleep(2)  # Simula um tempo entre os envios

producer.flush()  # Garante que todas as mensagens foram enviadas
print("Todas as transações foram enviadas!")
