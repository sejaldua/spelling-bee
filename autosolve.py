import itertools
import time
import pandas as pd
import pyautogui
try:
    from PIL import Image
except ImportError:
    import Image

import pytesseract
import cv2

with pyautogui.hold('command'):
    pyautogui.press('tab')


# # get letters via pytesseract
# im = pyautogui.screenshot('pyautogui_ss.png', region=(0,0, 1000, 1400))
# img_cv = cv2.imread(r'pyautogui_ss.png')
# img_rgb = cv2.cvtColor(img_cv, cv2.COLOR_BGR2RGB)
# string = pytesseract.image_to_string(img_rgb)
# print(string)

user_input = pyautogui.prompt('Please enter the puzzle letters, separated by commas\nIMPORTANT: enter the center letter last!\nExample: A, B, C, D, E, F, X')
letters = user_input.split(', ')
cl = letters[-1]

with pyautogui.hold('command'):
    pyautogui.press('tab')
    
pyautogui.typewrite(['a', 'b', 'c', 'enter'], interval=0.25)
print('here')

english_dict = pd.read_json('https://raw.githubusercontent.com/matthewreagan/WebstersEnglishDictionary/master/dictionary.json', orient="index").to_dict(orient="index")
english_words = set(english_dict.keys())
# english_words = set(words.words())

# viable_words = []
# for i in range(4, len(letters)+2):
#     for p in itertools.product(letters, repeat=i):
#         if cl in p and ''.join(p).lower() in english_words:
#             viable_words.append(''.join(p))
#             time.sleep(0.15)