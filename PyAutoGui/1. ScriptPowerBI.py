import pyautogui as pa
import time
import pyperclip as pc # Necessário para lidar com caracteres especiais
pa.PAUSE = 1 # Configuração de pausa para segurança entre comandos

pa.press('win') # Pressiona a tecla Windows
pa.write('chrome') # Digita 'chrome' para abrir o navegador
pa.press('ENTER') # Pressiona a tecla Enter
pa.write("https://app.powerbi.com/groups/09f2d653-0663-41a1-b34e-64e828c9b9f5/reports/90666205-f7a7-4b80-bdef-e704fb7c8321/e894d303be8965fc3749?experience=power-bi")
pa.press('ENTER') # Pressiona a tecla Enter

time.sleep(5) # Time de 5 segundos
pa.press('F11') # Coloca em modo de Tela Cheia
