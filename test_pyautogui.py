import pyautogui as pag
try:
    from PIL import Image
except ImportError:
    import Image

import pytesseract
import cv2

with pag.hold('command'):
    pag.press('tab')


# # get letters via pytesseract
# im = pag.screenshot('pag_ss.png', region=(0,0, 1000, 1400))
# img_cv = cv2.imread(r'pag_ss.png')
# img_rgb = cv2.cvtColor(img_cv, cv2.COLOR_BGR2RGB)
# string = pytesseract.image_to_string(img_rgb)
# print(string)

user_input = pag.prompt('Please enter the puzzle letters, separated by commas\nIMPORTANT: enter the center letter last!\nExample: A, B, C, D, E, F, X')
letters = user_input.split(', ')
print(letters)