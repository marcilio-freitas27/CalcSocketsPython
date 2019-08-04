# calc server UDP

import socket

sock_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
host = socket.gethostname()
port = 12345

sock_server.bind((host, port))

print('''Servidor de calculadora iniciado.
Aguardando a requisição de  operações.''')

while True:
    dados, addr = sock_server.recvfrom(1024)
    dados2, addr2 = sock_server.recvfrom(1024)
    dados3, addr3 = sock_server.recvfrom(1024)
    print('Estabelecida uma conexão: {}'.format(str(addr)))
    print("Mensagem recebida: {} entre {} e {}".format(dados.decode('ascii'),
            dados2.decode('ascii'),dados3.decode('ascii') ))

    if (dados.decode('ascii')).lower() == 'q':
        print("Saiu!")
        exit()
    elif (dados.decode('ascii')).lower() == 'adicao':
        print('Enviando resposta da adicao para o cliente.')
        sock_server.sendto(str(int(dados2 )+ int(dados3)).encode('ascii'), addr)
    elif (dados.decode('ascii')).lower() == 'subtracao':
        print('Enviando resposta da subtração para o cliente.')
        sock_server.sendto(str(int(dados2) - int(dados3)).encode('ascii'), addr)
    elif (dados.decode('ascii')).lower() == 'multiplicacao':
        print('Enviando resposta da multiplicação para o cliente.')
        sock_server.sendto(str(int(dados2) * int(dados3)).encode('ascii'), addr)
    elif (dados.decode('ascii')).lower() == 'divisao':
        print('Enviando resposta da divisão para o cliente.')
        sock_server.sendto(str(int(dados2) / int(dados3)).encode('ascii'), addr)

sock_server.close()
