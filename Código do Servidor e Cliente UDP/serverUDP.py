from socket import *

host = ''
porta = 5000

# Criando socket UDP
servidor = socket(AF_INET, SOCK_DGRAM)
servidor.bind((host, porta))

print(f"Servidor UDP aguardando mensagens na porta {porta}...")

while True:
    dados, endereco = servidor.recvfrom(1024)
    if not dados or dados == b'\x18':
        break
    print(f"{endereco}: {dados.decode()}")

servidor.close()
