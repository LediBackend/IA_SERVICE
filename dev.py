import subprocess
import time

COMMAND = "uvicorn src.main:app --port 4590 --reload"

while True:
    print("Iniciando Uvicorn...")
    process = subprocess.Popen(COMMAND, shell=True)
    
    try:
        process.wait()
    except KeyboardInterrupt:
        print("Servidor detenido manualmente.")
        process.terminate()
        break

    print("Reiniciando servidor en 5 segundos...")
    print(time.sleep(5))
    time.sleep(5)
