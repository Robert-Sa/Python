import pyautogui as pa
import time
import pyperclip as pc  # Necessário para lidar com caracteres especiais

# Configuração de pausa para segurança entre comandos
pa.PAUSE = 1

def abrir_navegador():
    """Abre o navegador Chrome usando o menu iniciar."""
    pa.press('win')  # Pressiona a tecla Windows
    pa.write('chrome')  # Digita 'chrome' para abrir o navegador
    pa.press('enter')  # Confirma a escolha

def acessar_url(url):
    """Acessa uma URL específica no navegador."""
    time.sleep(2)  # Espera o navegador abrir
    pc.copy(url)  # Copia a URL para a área de transferência
    pa.hotkey('ctrl', 'v')  # Cola a URL no navegador
    pa.press('enter')  # Pressiona Enter para carregar a página

def maximizar_tela():
    """Maximiza a tela do navegador usando o atalho F11."""
    time.sleep(5)  # Tempo para a página carregar (ajustável)
    pa.press('F11')  # Ativa o modo tela cheia

if __name__ == "__main__":
    # URL do relatório do Power BI
    url_power_bi = (
        "https://app.powerbi.com/groups/09f2d653-0663-41a1-b34e-64e828c9b9f5/"
        "reports/90666205-f7a7-4b80-bdef-e704fb7c8321/e894d303be8965fc3749?"
        "experience=power-bi"
    )
    
    abrir_navegador()
    acessar_url(url_power_bi)
    maximizar_tela()
