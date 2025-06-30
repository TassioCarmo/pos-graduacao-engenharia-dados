import json
import random
import time
from datetime import datetime, timezone
import uuid

from kafka import KafkaProducer

SLEEP_TIME = 1

def gerar_venda():

    user_id = random.randint(1, 1000)
    valor = random.uniform(1.5, 3000)

    venda = {
        "message_id": uuid.uuid4().hex,
        "message": {
            "id_venda": uuid.uuid4().hex,
            "user_id": user_id,
            "valor_venda": valor
        },
        # utc timestamp
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }
    return venda


def main():

    producer = KafkaProducer(
        bootstrap_servers="localhost:9092",
        value_serializer=lambda v: json.dumps(v).encode("utf-8"),
    )

    while True:
        dados_venda = gerar_venda()
        producer.send("vendas", value=dados_venda)
        print(f"Venda criada: {dados_venda}")
        time.sleep(SLEEP_TIME)


if __name__ == "__main__":
    main()
