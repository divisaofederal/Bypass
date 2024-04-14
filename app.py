from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Configurando as opções do Chrome para executar em modo headless e definindo o User Agent
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3')

# Inicializando o driver do Chrome
driver = webdriver.Chrome(options=chrome_options)

# URL para acessar
url = "https://www.instagram.com/"

try:
    # Acessando a página
    driver.get(url)
    
    # Verificando se o título da página contém "Instagram"
    if "Instagram" in driver.title:
        print("Página acessada com sucesso!")
    else:
        print("Falha ao acessar a página.")
except Exception as e:
    print("Erro:", e)
finally:
    # Fechando o driver
    driver.quit()