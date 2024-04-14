from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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

# Esperar até 10 segundos para o campo de nome de usuário estar disponível
username_field = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "input.form-control[placeholder='Username']"))
)

# Preencher o campo de nome de usuário
username_field.send_keys("Seyzalel")

# Preencher o campo de senha
password_field = driver.find_element(By.CSS_SELECTOR, "input.form-control[placeholder='Password']")
password_field.send_keys("17102005")

# Clicar no botão de login
login_button = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary.btn-block.px-4")
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