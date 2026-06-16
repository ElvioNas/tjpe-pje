

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
chrome_options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=chrome_options)

# Acessa o site
driver.get("https://homologacao-pje.app.tjpe.jus.br/h06-2g/home.seam")

time.sleep(2)

#Realizando Login no sistema#

driver.find_element(By.ID, "username").send_keys("02112357417")
time.sleep(2)
driver.find_element(By.ID, "password").send_keys("123")

time.sleep(2)
driver.find_element(By.ID, "btnEntrar").click()
time.sleep(2)
driver.find_element(By.CLASS_NAME, "botao-menu").click()
time.sleep(2)
driver.find_element(By.XPATH, "//a[contains(text(), 'Processo')]").click()
time.sleep(2)
driver.find_element(By.PARTIAL_LINK_TEXT, "Novo processo").click()
time.sleep(2)
driver.find_element(By.XPATH, "//span[contains(text(), 'Selecione')]").click()
time.sleep(2)
driver.find_element(By.XPATH, "//li[contains(text(), 'DIREITO PENAL')]").click()
time.sleep(2)
driver.find_element(By.XPATH, "//span[contains(text(), 'Selecione')]").click()
time.sleep(2)
driver.find_element(By.XPATH, "//li[contains(text(), 'Recife - TJPE')]").click()
time.sleep(2)
driver.find_element(By.XPATH, "//span[contains(text(), 'Selecione')]").click()
time.sleep(2)
driver.find_element(By.XPATH, "//li[contains(text(), 'AÇÃO CIVIL PÚBLICA (65)')]").click()
time.sleep(2)
driver.find_element(By.ID, "processoTrfForm:incluiProcessoButton").click()
time.sleep(2)
driver.find_element(By.ID, "r_processoAssuntoListList:0:j_id396:j_id397:j_id398").click()
time.sleep(2)
driver.find_element(By.XPATH, "//td[contains(text(), 'Partes')]").click()
time.sleep(2)

time.sleep(1000)





