import socket
import sys

arglen=len(sys.argv)
if arglen<2:
    print('Ejemplo: python2 servidor_echo.py 5000')
    exit()

puerto=int(sys.argv[1])
historial = open('historial_echo.txt', 'a')

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

servidor.bind(("", puerto))
servidor.listen(1)

print ('Esperando para conectarse')
cliente, cliente_addr = servidor.accept()

print ('conexion desde', cliente_addr)
historial.write('IP: '+ cliente_addr[0] + ' Puerto: ' + str(cliente_addr[1]) +' Data: \n')

while True:
    recibido = cliente.recv(1024)
    print ('recibido "%s"' % (recibido))
    historial.write(recibido + '\n')


    if recibido:
        if recibido.upper() == 'CERRAR':
            cliente.sendall('Cerrando la conexion')
            historial.close()
            cliente.close()       
            break

        print ("Enviando mensaje nuevamente al cliente")
        cliente.sendall(recibido)

    else:
        print ('No hay mas datos', cliente_addr)
        break