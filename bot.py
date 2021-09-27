import cv2
import numpy as np
import pyautogui

class Bot:
    def __init__(self):
        
        self.screen_actual = cv2.imread("champs/screenshot.png",cv2.IMREAD_UNCHANGED)
        self.result = cv2.matchTemplate(self.screen_actual, self.screen_actual, cv2.TM_CCOEFF_NORMED)
        self.screen_list = ["champs/picking.png","champs/banning.png"]
        self.threshold = 0.6
        self.buttonw = 0
        self.buttonh = 0
        self.xloc = []
        self.yloc = []
        self.xloc_button = []
        self.yloc_button = []

        self.maxLoc = []
        self.minLoc = []
        self.minVal = []
        self.maxVal = []


    #CHECKS WHERE YOU ARE LOOKING, HOME, CHAMPION SELECT, PREPAIRING RUNES.
    def checkScreenStatus(self,screen_updated):
        for i in range(len(self.screen_list)):

            screen_actual = cv2.imread(self.screen_list[i],cv2.IMREAD_UNCHANGED)
            result = cv2.matchTemplate(screen_updated, screen_actual, cv2.TM_CCOEFF_NORMED)
            xloc,yloc = np.where(result >= self.threshold)

            if(len(xloc) != 0): 
                return i

    #UPDATE WHAT YOU ARE LOOKING, AND EXPORT TO IMG.
    def updateScreen(self,lol_window):
        myScreenshot = pyautogui.screenshot()
        myScreenshot.save(r'champs/screenshot.png')
        screen_updated = cv2.imread("champs/screenshot.png",cv2.IMREAD_UNCHANGED)
        return screen_updated


    #SEARCH FOR THE BUTTON OR IMG THAT HAS BEEN PASSED, AND CHECK IF IS THERE
    def searchImage(self,screen_updated,img):

        #GET THE ACCEPT BUTTON AND COMPARE TO THE ACTUAL SCREEN
        accept_button = cv2.imread(img,cv2.IMREAD_UNCHANGED)
        accept_result = cv2.matchTemplate(screen_updated, accept_button, cv2.TM_CCOEFF_NORMED)

        #GET ALL LOCATIONS OF THE BUTTON IN THE SCREEN
        self.minVal,self.maxVal,self.minLoc,self.maxLoc = cv2.minMaxLoc(accept_result)
        self.xloc_button,self.yloc_button = np.where(accept_result >= self.threshold)
        
        x,y = self.maxLoc

        #IF AN OBJECT HAS BEEN ALOCATED  GET THE SIZE OF THE ACCEPT BUTTON AND CLICK ON IT
        if(len(self.yloc_button) != 0):
            jugarw = accept_button.shape[1]
            jugarh = accept_button.shape[0]
            pyautogui.click((jugarw / 2) + x,(jugarh / 2)+y)
            pyautogui.click((jugarw / 2) + x,(jugarh / 2)+y)





            
