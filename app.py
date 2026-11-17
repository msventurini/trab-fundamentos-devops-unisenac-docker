import time
import redis
from flask import Flask
from datetime import datetime

app = Flask(__name__)
cache = redis.Redis(host='banco-redis', port=6379)

def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)

@app.route('/')
def hello():
    count = get_hit_count()
    mensagem = f'Olá! Esta página foi vista {count} vezes.\n'
    # Gravando no log
    with open('/var/log/app/acessos.log', 'a') as f:
        f.write(f'Acesso numero {count} em {datetime.now()}\n')
    return mensagem

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)