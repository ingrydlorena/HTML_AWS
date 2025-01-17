import pyautogui,time

time.sleep(10)

# Obtém a posição atual do cursor
posicao = pyautogui.position()

print(f'A posição atual do mouse é: {posicao}')