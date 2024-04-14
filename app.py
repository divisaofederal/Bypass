from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Inicializar o navegador em modo headless
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Executar em modo headless, sem interface gráfica
options.add_argument('--disable-gpu')  # Necessário para Chrome em Linux
driver = webdriver.Chrome(options=options)

# Abrir o Instagram
driver.get("https://www.instagram.com/")

# Esperar um momento para garantir que a página seja carregada completamente
time.sleep(4)

# Encontrar os campos de login e senha e preenchê-los
username_field = driver.find_element_by_name('username')
password_field = driver.find_element_by_name('password')
username_field.send_keys('seyzalel')
password_field.send_keys('Sey17zalel17@$')

# Enviar o formulário de login
password_field.send_keys(Keys.RETURN)

# Esperar um pouco para o login ser processado
time.sleep(7)

# Verificar se o login foi bem sucedido
if "feed" in driver.current_url:
    print("Login bem sucedido!")
else:
    print("Login falhou.")

# Fechar o navegador
driver.quit()