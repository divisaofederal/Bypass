from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configurações do WebDriver
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Executar em segundo plano
driver = webdriver.Chrome(options=options)

# URL da página
url = "https://stresse.net/"

try:
    # Acessar a página
    driver.get(url)
    
    # Esperar até que o botão esteja visível
    button = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//a[@class='menu-link btn btn-primary btn-round' and @href='/home']"))
    )
    
    # Clicar no botão
    button.click()
    
    # Verificar se o botão foi clicado
    if "home" in driver.current_url:
        print("O botão ATTACK HUB foi clicado com sucesso.")
    else:
        print("Falha ao clicar no botão ATTACK HUB.")
        
except Exception as e:
    print("Ocorreu um erro:", e)

finally:
    # Fechar o navegador
    driver.quit()