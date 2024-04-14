from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# Configurando as opções do Chrome para headless
options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--disable-gpu")  

# Inicializando o driver do Chrome
driver = webdriver.Chrome(options=options)

# Navegando até a página de login do Instagram
driver.get("https://www.instagram.com/")

# Preenchendo os campos de usuário e senha
username = "seu_usuario"
password = "sua_senha"

# Aguardando a presença do campo de usuário
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='username']")))

# Preenchendo o campo de usuário
driver.find_element(By.CSS_SELECTOR, "input[name='username']").send_keys(username)

# Preenchendo o campo de senha
driver.find_element(By.CSS_SELECTOR, "input[name='password']").send_keys(password)

# Aguardando o botão de login estar habilitado
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))

# Enviando o formulário de login
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

try:
    # Aguardando a presença do botão "Agora não"
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.x1i10hfl")))
    print("Login bem sucedido!")

    # Acessando a conta fornecida
    account_url = "https://www.instagram.com/iihgabss"
    driver.get(account_url)

    # Verificando se a conta foi acessada com sucesso
    WebDriverWait(driver, 10).until(EC.url_to_be(account_url))
    print("Conta acessada com sucesso:", account_url)
except TimeoutException:
    print("Falha no login. Verifique suas credenciais ou a URL da conta.")

# Finalizando o driver
driver.quit()