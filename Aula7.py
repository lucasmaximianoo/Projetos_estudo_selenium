from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver import ChromeOptions, Chrome
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


opts = ChromeOptions()  #esta opcao serve para nao fechar o navegador apos a execucao do script
opts.add_experimental_option("detach", True)
servico=Service(ChromeDriverManager().install())
driver=webdriver.Chrome(service=servico, options=opts)


driver.get("https://statusinvest.com.br/fundos-imobiliarios/knri11")
driver.implicitly_wait(3)

for i in range(5):
    dados = driver.find_elements(By.CLASS_NAME,"value")[i].text
    print(dados)
    print('------')
else:
    print('Algo deu errado')
