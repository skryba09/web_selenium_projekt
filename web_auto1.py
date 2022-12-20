import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#Strona pozostaje otwarta po uruchomieniu drivera
s = Service("C:/Users/Iwo/Desktop/chromedriver.exe")
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

#Tworze obiekt driver na ktorym moge operowac wszystkimi metodami klasy webdriver
driver = webdriver.Chrome(service=s, options=chrome_options)

#Otwiera strone
driver.get("https://www.google.com")
driver.maximize_window()

#Potwierdzenie cookies
agree = driver.find_element(By.ID, 'L2AGLb')
agree.click()

#Klikam w pasek wyszukiwania
driver.implicitly_wait(5)
element_search_bar = driver.find_element(By.NAME, 'q')
element_search_bar.click()

#Przekazuje tekst do paska wyszukiwania
odpowiedz = input("Co chcesz wyszukac?: ")
element_search_bar.send_keys(odpowiedz)
element_search_bar.submit()

#Wyłapuje wszystkie linki ze strony i wyswietlam je uzytkownikowi
wyniki = driver.find_elements(By.CLASS_NAME, 'yuRUbf')
tabela = []
for i, x in enumerate(wyniki):
    x = wyniki[i].find_element(By.TAG_NAME, 'a')
    href = x.get_attribute("href")
    print(href)
    tabela.append(href)
tabela = list(dict.fromkeys(tabela))
print(tabela)


#Scrollowanie strony
def scrolluj_dol():
    driver.execute_script("window.scrollBy(0,800)","")
def scrolluj_gora():
    driver.execute_script("window.scrollBy(0,-800)","")

for x in range(5):
    wybor = input("czy scrollowac w dol: ")
    if wybor == "tak":
        scrolluj_dol()
    elif wybor == "nie":
        scrolluj_gora()

numer = int(input("Ktory wynik cie interesuje, wybierz: "))
driver.get(tabela[numer])
