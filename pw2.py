import time
from test import Strona

liczby = ['pierwszy','drugi', 'trzeci',
           'czwarty', 'piąty', 'szósty',
           'siódmy', 'ósmy', 'dziewiąty']

bot = Strona()
bot.strona_glowna()

wyszukanie = input("Co chcesz wyszukac?:")
link = input("Ktory link wybrac? ")

a = bot.wyszukiwarka(wyszukanie)
print(len(a))
bot.wybor_wyniku(a, link)
bot.scrolluj_dol()
b, c = bot.aktualnosci()
wybor = input("Podaj stringa") #Wystarczy ze podamy fragment stringa do ktorego chcemy dopasowac
bot.wybiersz_aktualnosc(b,c,wybor)
time.sleep(4)
bot.driver.back()


# for x in range(5):
#     wybor = input("czy scrollowac w dol: ")
#     if wybor == "tak":
#         bot.scrolluj_dol()
#     elif wybor == "nie":
#         bot.scrolluj_gora()
