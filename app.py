from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
    
    # Encontrando campos de login e senha
    username_field = driver.find_element_by_name("username")
    password_field = driver.find_element_by_name("password")
    
    # Preenchendo os campos de login e senha
    username_field.send_keys("seyzalel")
    password_field.send_keys("Sey17zalel17@$")
    
    # Esperando até que o botão de login esteja habilitado
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//button[@type="submit"]'))
    )
    
    # Clicando no botão de login
    login_button.click()
    
    # Verificando se o login foi bem-sucedido
    if "/accounts/onetap" in driver.current_url:
        print("Login realizado com sucesso.")
    else:
        print("Falha no login.")
    
except Exception as e:
    print("Erro:", e)
finally:
    # Fechando o driver
    driver.quit()