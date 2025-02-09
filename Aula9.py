from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver import ChromeOptions, Chrome
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

opts = ChromeOptions()  #esta opcao serve para nao fechar o navegador apos a execucao do script
opts.add_experimental_option("detach", False)
servico=Service(ChromeDriverManager().install())
driver=webdriver.Chrome(service=servico, options=opts)


driver.get("https://www.imdb.com/")
driver.implicitly_wait(3)

input = driver.find_elements(By.NAME,"q")[0]

input.send_keys("Velozes e Furiosos 2")
sleep(5)