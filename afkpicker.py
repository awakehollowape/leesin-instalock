import pygetwindow as gw
import cv2
import numpy as np
import pyautogui
import bot
import time



bot = bot.Bot()
buttons = ["search.png","lock.png","accept.png"]
primary_champion = ""




def main():
    print("Que onda pa, te vas a hacer una pajita?, Tranqui te suporteo.")
    primary_champion = input("Decime que te pickeo(leesin): ") 
    champ = primary_champion + ".png"

    while True:
        lol_window = gw.getWindowsWithTitle('League of Legends')[0]
        screen_updated = cv2.imread("screenshot.png",cv2.IMREAD_UNCHANGED)
        bot.updateScreen(lol_window)

        bot.searchImage(bot.updateScreen(lol_window),buttons[2])

        if(bot.checkScreenStatus(bot.updateScreen(lol_window)) == 0):
            print("Estamos pickeando..")
            bot.searchImage(bot.updateScreen(lol_window),buttons[0])

            pyautogui.typewrite(primary_champion)
            time.sleep(5)
            bot.searchImage(bot.updateScreen(lol_window),champ)
            
            bot.searchImage(bot.updateScreen(lol_window),buttons[1])



        if(bot.checkScreenStatus(bot.updateScreen(lol_window)) == 1):
            print("Estamos baneando..")
        



if __name__ == "__main__":
    # execute only if run as a script
    main()





    #Cosas a arreglar#
    #Cuando pickeo tiene que reconocer la imagen mia + el tiempo de la isquierda para saber si estoy pickeando
    # solo tiene que pegar 1 sola vez el nombre del campeon poner un stop con una imagen nueva o algo asi
    # para detectar si el campeon esta baneado podemos revisar la parte de arriba del cliente o sino la imagen del campeon en gris#
    # clickear en la imagen y lockear

