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
driver.get("https://stresse.net/login")

# Preenchendo os campos de usuário e senha
username = "Selazar"
password = "17102005"

try:
    # Aguardando a presença do campo de usuário
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.NAME, "username")))

    # Preenchendo o campo de usuário
    driver.find_element(By.NAME, "username").send_keys(username)

    # Preenchendo o campo de senha
    driver.find_element(By.NAME, "password").send_keys(password)

    # Localizando e clicando no botão de login
    driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary.btn-block.px-4").click()

    # Aguardando o redirecionamento para a página inicial
    WebDriverWait(driver, 20).until(EC.url_to_be("https://stresse.net/home"))

    print("Login bem sucedido! Conta acessada com sucesso.")

except TimeoutException:
    print("Falha no login. Verifique suas credenciais ou a URL da conta.")

# Finalizando o driver
driver.quit()