import sys
import json
from servidor import Servidor

with open('parametros.json', 'r', encoding='utf-8') as file:
    p = json.load(file)

if __name__ == "__main__":
    servidor = Servidor(p['host'], p['port'])

    try:
        while True:
            input("[Presione Ctrl+C para cerrar el servidor]  ")
    except KeyboardInterrupt:
        print("\nCerrando servidor...")
        servidor.socket_servidor.close()
        sys.exit()
