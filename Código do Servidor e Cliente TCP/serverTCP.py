from socket import *

host = ''
porta = 5001

# Criando socket TCP
servidor = socket(AF_INET, SOCK_STREAM)
servidor.bind((host, porta))
servidor.listen(1)

print(f"Servidor TCP esperando conexão na porta {porta}...")

while True:
    conexao, endereco = servidor.accept()
    print(f"Cliente conectado: {endereco}")

    while True:
        dados = conexao.recv(1024)
        if not dados or dados == b'\x18':
            break
        print(f"{endereco}: {dados.decode()}")
    break

print("Encerrando conexão com", endereco)
conexao.close()
