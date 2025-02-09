from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import Select

from selenium.webdriver.common.by import By
from selenium.webdriver import ChromeOptions, Chrome

#Chrome
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

opts = ChromeOptions()
#esta opcao serve para nao fechar o navegador apos a execucao do script
opts.add_experimental_option("detach", True)
servico=Service(ChromeDriverManager().install())
driver=webdriver.Chrome(service=servico, options=opts)

import pandas as pd

planilha = []
linha = []

driver.get("https://www.melhorcambio.com/euro-hoje")

sleep(6)

elementoMoeda = Select(driver.find_element(By.ID, 'currency-1'))
elementoMoeda.select_by_value('dolar')
#moeda.select_by_visible_text('Dólar')

elementoCidade = Select(driver.find_element(By.NAME, 'cities'))

for i in range(100):
    elementoCidade.select_by_index(i)
    sleep(3)
    cidade = driver.find_element(By.CLASS_NAME, 'currency-today-select-cities-select-container').text
    linha.append(cidade)
    
    valorTurismo = driver.find_element(By.ID, 'currency-today-tourism-amount').text
    linha.append(valorTurismo)
    
    iofTurismo = driver.find_element(By.ID, 'currency-today-tourism-iof').text
    linha.append(iofTurismo)
    
    taxaOperacional = driver.find_element(By.ID, 'currency-today-tourism-tax').text
    linha.append(taxaOperacional)
    
    valorFinal = driver.find_element(By.ID, 'currency-today-tourism-total').text
    linha.append(valorFinal)
    
    planilha.append(linha)
    linha = []
    
df = pd.DataFrame(planilha)
df.columns = ['Cidade', 'Dólar turismo','IOF: 1,1%','Taxa operacional', 'Valor final']

sorted_data = df.sort_values(by='Valor final', ascending=True)

sorted_data.to_excel("C:/Users/User/Downloads/cambio2.xlsx")
print("Salvei o arquivo")
    













