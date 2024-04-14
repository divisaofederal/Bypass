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

# Navegando até a página de login do stresse.net
driver.get("https://stresse.net/login")

# Preenchendo os campos de usuário e senha
username = "Selazar"
password = "17102005"

# Preenchendo o campo de usuário
driver.find_element(By.CSS_SELECTOR, "input[placeholder='Username']").send_keys(username)

# Preenchendo o campo de senha
driver.find_element(By.CSS_SELECTOR, "input[placeholder='Password']").send_keys(password)

# Clicando no botão de login
driver.find_element(By.CSS_SELECTOR, "button.btn-primary").click()

try:
    # Aguardando o redirecionamento para a página principal após o login
    WebDriverWait(driver, 10).until(EC.url_to_be("https://stresse.net/home"))
    print("Login bem sucedido!")
except TimeoutException:
    print("Falha no login. Verifique suas credenciais.")

# Finalizando o driver
driver.quit()