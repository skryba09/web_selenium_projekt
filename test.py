import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


# wyszukanie = input("Co chcesz wyszukac?:")
# link = input("Ktory link wybrac? ")

# s = Service("C:/Users/Iwo/Desktop/chromedriver.exe")
# opcje_google_chrome = Options()
# opcje_google_chrome.add_experimental_option("detach", True)
liczby = ['pierwszy','drugi', 'trzeci',
           'czwarty', 'piąty', 'szósty',
           'siódmy', 'ósmy', 'dziewiąty']



class Strona():

    s = Service("C:/Users/Iwo/Desktop/chromedriver.exe")
    opcje_google_chrome = Options()
    opcje_google_chrome.add_experimental_option("detach", True)

    def __init__(self, driver = webdriver.Chrome(service=s, options=opcje_google_chrome)):
        self.driver = driver

    def strona_glowna(self):
        self.driver.get("https://www.google.com")
        self.driver.maximize_window()
        akceptuj = self.driver.find_element(By.ID, 'L2AGLb')
        akceptuj.click()

    def scrolluj_dol(self):
        self.driver.execute_script("window.scrollBy(0,900)", "")

    def scrolluj_gora(self):
        self.driver.execute_script("window.scrollBy(0,-900)", "")

    #Zapytanie co chcesz wyszukac wyszukanie = input("Co chcesz wyszukac?: ")
    def wyszukiwarka(self, wyszukanie):
        self.driver.implicitly_wait(5)
        wyszukaj = self.driver.find_element(By.NAME, 'q') #zrobic chyba implicit/explicit waita
        wyszukaj.send_keys(wyszukanie)
        wyszukaj.submit()
        wyniki = self.driver.find_elements(By.CLASS_NAME, 'yuRUbf')
        tabela = []
        for i, x in enumerate(wyniki):
            x = wyniki[i].find_element(By.TAG_NAME, 'a')
            href = x.get_attribute("href")
            print(href)
            tabela.append(href)
        tabela = list(dict.fromkeys(tabela))
        return tabela

    #Zapytanie jaki link wybrac? link = input("")
    def wybor_wyniku(self, tabela, link):
        print(liczby)
        if link in liczby:
            idx = liczby.index(link)
            self.driver.get(tabela[idx])
        else:
            print("Nie ma takiego stringa")

    #Mowimy ze chcemy otworzyc aktualnosci, wyrzuca wszystkie do tabelki
    def aktualnosci(self):
        lista1 = self.driver.find_element(By.CSS_SELECTOR, ".col-12.col-md-10.col-lg-12 [href]")
        link = lista1.get_attribute('href')
        self.driver.get(link)

        ramki = self.driver.find_elements(By.CSS_SELECTOR, ".card.h-100 [href]")
        # print(ramki)
        tabelka = [x.get_attribute("href") for x in ramki]  # bardzo dobrze zrobione list comprehensive
        nazwy = [x.text.strip() for x in ramki]
        print(nazwy)
        return tabelka, nazwy

    #Bot sie pyta która aktualnosc wybrac, wybor
    def wybiersz_aktualnosc(self, tabelka, nazwy, wybor):
        #tabelka:lista, zwrocilo nam liste
        #nazwy:lista
        #wybor to string, wybor uzytkownika
        for i, x in enumerate(nazwy):
            if wybor in x:
                #idx = nazwy.index(x)
                self.driver.get(tabelka[i])
                break
            if wybor not in x and i == len(nazwy)-1:
                print("Nie ma takiego elementu w liscie!")
                break




    # nowy_wynik = [x.split("/").pop(-1).replace("-", " ") for x in wynik]  # kolejny dobry list comprehension
    # polacz = ''.join(stan)
    # odp = zmiana(polacz)
    # odp = odp.split("/")
    # odp.pop(-1)
    # odp = '/'.join(odp)














# bot = Strona()
# bot.strona_glowna()
# a = bot.wyszukiwarka(wyszukanie)
# print(len(a))
# bot.wybor_wyniku(a)

#To trzeba bedzie przetestowac i pododawac do wyszukiwania elementow
# akceptuj = WebDriverWait(self.driver, 10).until(
#     EC.presence_of_element_located((By.ID, 'L2AGLb'))
# )