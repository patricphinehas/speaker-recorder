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
    template3 = cv2.imread('/images/template3.png', 0)
    template4 = cv2.imread('/images/template4.png', 0)
    template5 = cv2.imread('/images/template5.png', 0)
    template6 = cv2.imread('/images/template6.png', 0)
except expression as identifier:
    print("error loading images for comaprison")

# image matching threshold
threshold = 0.7

# alert for the closure of the application
pyautogui.alert(text='Keep the mouse pointer on the top left corner of screen to stop the program',
                title='Stopping Criteria')


# continuous loop to check for youtube ad
while True:
    time.sleep(1)
    im1 = pyautogui.screenshot()
    im1 = np.asarray(im1.convert(mode = 'L'))
#     im1.save('im1.png')
#     im1 = cv2.imread('im1.png', 0)
        
# checking for template3   
    res = cv2.matchTemplate(im1, template3, cv2.TM_CCOEFF_NORMED)
    loc = np.where(res >= threshold)
    
# checking if template is matched
    if loc[0].size != 0:
# clicking on the first match
        pyautogui.click(list(zip(*loc[::-1]))[0])
        continue # continue loop from start without further execution of the loop
        
# checking for template4      
    res = cv2.matchTemplate(im1, template4, cv2.TM_CCOEFF_NORMED)
    loc = np.where(res >= threshold)
    
# checking if template is matched
    if loc[0].size != 0:
# clicking on the first match
        pyautogui.click(list(zip(*loc[::-1]))[0])
        continue # continue loop from start without further execution of the loop
        
# checking for template5        
    res = cv2.matchTemplate(im1, template5, cv2.TM_CCOEFF_NORMED)
    loc = np.where(res >= threshold)
    
# checking if template is matched
    if loc[0].size != 0:
# clicking on the first match
        pyautogui.click(list(zip(*loc[::-1]))[0])
        continue # continue loop from start without further execution of the loop    
    
# checking for template6        
    res = cv2.matchTemplate(im1, template6, cv2.TM_CCOEFF_NORMED)
    loc = np.where(res >= threshold)
    
# checking if template is matched
    if loc[0].size != 0:
# clicking on the first match
        pyautogui.click(list(zip(*loc[::-1]))[0])
    
#     Stopping criteria
    if pyautogui.position() == (0,0):
    	pyautogui.alert(text = 'Adskipper is Closed', title = 'Adskipper Closed')
    	break