# calc client UDP

import socket

sock_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
host = socket.gethostname()
port = 12345

sock = ((host, port))

print('*'*60+'SoCalcPy'+'*'*60)
print('''Escolha umas das operações e de Enter; o primeiro valor, Enter; o segundo, Enter:

    -adicao;
    -subtracao;
    -multiplicacao;
    -divisao.

Digite 'q' e de Enter para sair.''')

msg = input('-->')
if msg == 'q':
    sock_client.sendto(msg.encode('ascii'), sock)
    msg2 = 'q'
    sock_client.sendto(msg2.encode('ascii'), sock)
    msg3 = 'q'
    sock_client.sendto(msg3.encode('ascii'), sock)
    print("Saiu!")
    sock_client.close()

else:
    msg2 = input('-->')
    msg3 = input('-->')

while msg != 'q':
    sock_client.sendto(msg.encode('ascii'), sock)
    sock_client.sendto(msg2.encode('ascii'), sock)
    sock_client.sendto(msg3.encode('ascii'), sock)
    print("Mensagem Enviada: qual o resultado da {} entre {} e {}?".format(msg, msg2,msg3))
    dados, end = sock_client.recvfrom(1024)

    print('Resposta: {}'.format(dados.decode('ascii')))
    msg = input('-->')
    if msg == 'q':
        sock_client.sendto(msg.encode('ascii'), sock)
        msg2 = 'q'
        sock_client.sendto(msg2.encode('ascii'), sock)
        msg3 = 'q'
        sock_client.sendto(msg3.encode('ascii'), sock)
        print("Saiu!")
        sock_client.close()

    else:
        msg2 = input('-->')
        msg3 = input('-->')

sock_client.close()
