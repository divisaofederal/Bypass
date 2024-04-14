import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains  # Importando ActionChains

# Configurando as opções do Chrome para executar em modo headless e definindo o User Agent
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3')
chrome_options.add_argument('--window-size=1920,1080')  # Resolução da tela
chrome_options.add_argument('--disable-notifications')  # Desativar notificações
chrome_options.add_argument('--disable-infobars')  # Desativar infobars
chrome_options.add_argument('--disable-dev-shm-usage')  # Desativar uso de memória compartilhada do sistema
chrome_options.add_argument('--no-sandbox')  # Execução sem sandbox
chrome_options.add_argument('--disable-gpu')  # Desativar aceleração de GPU
chrome_options.add_argument('--disable-extensions')  # Desativar extensões do Chrome
chrome_options.add_argument('--disable-web-security')  # Desativar segurança web
chrome_options.add_argument('--allow-running-insecure-content')  # Permitir execução de conteúdo inseguro

# Inicializando o driver do Chrome
driver = webdriver.Chrome(options=chrome_options)

# URL para acessar
url = "https://stresse.net/login"

try:
    # Acessando a página
    driver.get(url)
    
    # Esperando até que os campos de login e senha estejam presentes
    username_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type="text"][placeholder="Username"]'))
    )
    password_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type="password"][placeholder="Password"]'))
    )
    
    # Preenchendo os campos de login e senha
    username_field.send_keys("Selazar")
    time.sleep(random.uniform(1, 2))  # Atraso entre 1 e 2 segundos
    password_field.send_keys("17102005")
    time.sleep(random.uniform(1, 2))  # Atraso entre 1 e 2 segundos
    
    # Simulando movimento do mouse antes de clicar no botão de login
    ActionChains(driver).move_by_offset(random.randint(50, 100), random.randint(50, 100)).perform()
    time.sleep(random.uniform(1, 2))  # Atraso entre 1 e 2 segundos
    
    # Esperando até que o botão de login esteja habilitado
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//button[contains(@class, "btn-primary")][contains(text(), "Login")]'))
    )
    
    # Clicando no botão de login
    login_button.click()
    
    # Verificando se o título da página contém "Home" após 10 segundos
    WebDriverWait(driver, 10).until(
        EC.title_contains("Home")
    )
    
    print("Login realizado com sucesso.")
    
    # Aguardando 6 segundos antes de clicar no primeiro elemento
    time.sleep(6)
    
    # Tentando encontrar e clicar no primeiro elemento
    try:
        first_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'a.animated-arrow'))
        )
        first_element.click()
        print("Clique no primeiro elemento bem-sucedido.")
    except Exception as e:
        print("Falha ao clicar no primeiro elemento:", e)
    
    # Aguardando mais 6 segundos antes de clicar no segundo elemento
    time.sleep(6)
    
    # Tentando encontrar e clicar no segundo elemento
    try:
        second_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//a[contains(@href, "/panel")]'))
        )
        second_element.click()
        print("Clique no segundo elemento bem-sucedido.")
    except Exception as e:
        print("Falha ao clicar no segundo elemento:", e)
    
except Exception as e:
    print("Falha no login:", e)
finally:
    # Fechando o driver
    driver.quit()