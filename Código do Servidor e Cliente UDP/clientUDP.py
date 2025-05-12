from socket import *

host = '127.0.0.1'
porta = 5000

cliente = socket(AF_INET, SOCK_DGRAM)

print("Cliente UDP.\nDigite mensagens (CTRL+X para sair):")

mensagem = ''
while mensagem != '\x18':
    mensagem = input()
    cliente.sendto(mensagem.encode(), (host, porta))

cliente.close()
