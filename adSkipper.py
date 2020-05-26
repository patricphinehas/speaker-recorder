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
pyautogui.alert(text = 'Keep the mouse pointer on the top left corner of screen to stop the program', title= 'Stopping Criteria')

while True:
    time.sleep(1)
    im1 = pyautogui.screenshot()
    im1 = np.asarray(im1.convert(mode = 'L'))
