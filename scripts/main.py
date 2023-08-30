from selenium import webdriver

from selenium.webdriver.common.by import By

def get_action_value(action):
    """
    Obtém as informações da tela do Google Chrome.

    Returns:
        O valor da ação obtido a partir do XPath especificado.
    """

    # Inicializar o driver do Chrome
    driver = webdriver.Chrome()

    # Abrir a página do Google
    driver.get(f"https://www.google.com/search?q={action}")

    xpath_value = '//*[@id="knowledge-finance-wholepage__entity-summary"]/div[3]/g-card-section/div/g-card-section/div[2]/div[1]/span[1]/span/span[1]'
    xpath_title = '//*[@id="rcnt"]/div[2]/div/div/div[3]/div[1]/div/div/div/div[1]/div/div'
    value_action = ''
    title_action = ''
    try:
        # Encontrar o elemento usando o XPath especificado
        value = driver.find_element(By.XPATH, xpath_value)
        title = driver.find_element(By.XPATH, xpath_title)
        # Extrair o valor de texto do elemento
        value_action = value.text
        title_action = title.text
        
    except Exception as e:
        
        return f'Erro ao obter o valor da ação: {e}'
    
    # Fechar o navegador
    driver.quit()
    
    return value_action, title_action

def main():
    """
    Programa principal.
    """

    # Obtém o valor da ação
    value = get_action_value(action='VGIR11')
    
    print(value)

main()
