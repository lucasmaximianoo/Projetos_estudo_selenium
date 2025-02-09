from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

#Chrome
from selenium.webdriver import ChromeOptions, Chrome
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

opts = ChromeOptions() #esta opcao serve para nao fechar o navegador apos a execucao do script
opts.add_experimental_option("detach", True)
servico=Service(ChromeDriverManager().install())
driver=webdriver.Chrome(service=servico, options=opts)

driver.get("https://www.infomoney.com.br/")

driver.implicitly_wait(10) #segundos

dados1 = driver.find_elements(By.TAG_NAME, "table")[0].text
print("--------------")
print(dados1)
print("--------------")
