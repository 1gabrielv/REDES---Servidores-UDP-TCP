from socket import *

host = '127.0.0.1'
porta = 5001

cliente = socket(AF_INET, SOCK_STREAM)
cliente.connect((host, porta))

print("Conectado ao servidor TCP.\nDigite mensagens (CTRL+X para sair):")

mensagem = ''
while mensagem != '\x18':
    mensagem = input()
    cliente.send(mensagem.encode())

cliente.close()