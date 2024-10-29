import pyautogui as pa
import time
import pyperclip
pa.PAUSE = 1

pa.press('win')
pa.write('chrome')
pa.press('ENTER')
pa.write("https://app.powerbi.com/groups/09f2d653-0663-41a1-b34e-64e828c9b9f5/reports/90666205-f7a7-4b80-bdef-e704fb7c8321/e894d303be8965fc3749?experience=power-bi")
pa.press('ENTER')

time.sleep(5)
pa.press('F11')