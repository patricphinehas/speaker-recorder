import cv2
import numpy as np
import pyautogui
import time

# all images load
# flag
# 1 -> color
# 0 -> grayscale
# -1 -> unchanged Alpha channel replication


try:
    template3 = cv2.imread('./images/template3.png', 0)
    template4 = cv2.imread('./images/template4.png', 0)
    template5 = cv2.imread('./images/template5.png', 0)
    template6 = cv2.imread('./images/template6.png', 0)
    template7 = cv2.imread('./images/template7.png', 0)
except expression as identifier:
    print("error loading images for comaprison")

# image matching threshold
threshold = 0.7

def skipper():
    pyautogui.alert(text='Keep the mouse pointer on the top left corner of screen to stop the program', title='Stopping Criteria')
    
    while True:
        time.sleep(1)
        im1 = pyautogui.screenshot()
        im1 = np.asarray(im1.convert(mode='L'))

        res = cv2.matchTemplate(im1, template3, cv2.TM_CCOEFF_NORMED)
        loc = np.where(res >= threshold)
        if loc[0].size != 0:
            pyautogui.click(list(zip(*loc[::-1]))[0])
            continue

        res = cv2.matchTemplate(im1, template4, cv2.TM_CCOEFF_NORMED)
        loc = np.where(res >= threshold)
        if loc[0].size != 0:
            pyautogui.click(list(zip(*loc[::-1]))[0])
            continue

        res = cv2.matchTemplate(im1, template5, cv2.TM_CCOEFF_NORMED)
        loc = np.where(res >= threshold)
        if loc[0].size != 0:
            pyautogui.click(list(zip(*loc[::-1]))[0])
            continue

        res = cv2.matchTemplate(im1, template6, cv2.TM_CCOEFF_NORMED)
        loc = np.where(res >= threshold)
        if loc[0].size != 0:
            pyautogui.click(list(zip(*loc[::-1]))[0])
            continue

        # res = cv2.matchTemplate(im1, template7, cv2.TM_CCOEFF_NORMED)
        # loc = np.where(res >= threshold)
        # if loc[0].size != 0:
        #     # pyautogui.alert(text='i Just found the auto play, Voila!', title='found autoplay')
        #     print("found autoplay")
        #     continue
    

        if pyautogui.position() == (0, 0):
            pyautogui.alert(text='Adskipper is Closed', title='Adskipper Closed')
            break
