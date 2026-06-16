from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
chrome_options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=chrome_options)

# Acessa o site
driver.get("https://homologacao-pje.app.tjpe.jus.br/h06-1g/home.seam")
time.sleep(2)
driver.find_element(By.XPATH, "//a[contains(text(), 'Consulta processual')]").click()
time.sleep(2)
driver.get("https://homologacao-pje.app.tjpe.jus.br/h06-2g/ConsultaPublica/listView.seam")
time.sleep(2)
driver.find_element(By.ID, "fPP:dnp:nomeParte").send_keys("João Pedro")
time.sleep(2)
driver.find_element(By.ID, "fPP:searchProcessos").click()
time.sleep(2)



time.sleep(1000)