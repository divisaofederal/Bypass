from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

# Configurações do Selenium para execução headless no ambiente render
chrome_options = Options()
chrome_options.add_argument("--headless")  # Execução headless
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--remote-debugging-port=9222")
chrome_options.add_argument("--single-process")

# Inicialização do driver
driver = webdriver.Chrome(options=chrome_options)

# URL do site
url = "https://stresse.net/login"

# Acessar a URL
driver.get(url)

# Esperar até 10 segundos para qualquer elemento estar disponível
driver.implicitly_wait(10)

# Preencher o campo de nome de usuário
username_field = driver.find_element_by_css_selector("input[name='username']")
username_field.send_keys("Seyzalel")

# Preencher o campo de senha
password_field = driver.find_element_by_css_selector("input[name='password']")
password_field.send_keys("17102005")

# Clicar no botão de login
login_button = driver.find_element_by_css_selector("button.btn.btn-primary.btn-block.px-4")
login_button.click()

# Esperar um tempo para o redirecionamento
time.sleep(5)

# Verificar se a URL foi redirecionada corretamente
if driver.current_url == "https://stresse.net/home":
    print("Login realizado com sucesso!")
else:
    print("Falha ao realizar login!")

# Encerrar o driver
driver.quit()