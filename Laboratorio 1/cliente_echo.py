import socket
import sys

arglen=len(sys.argv)
if arglen<3:
    print('Ejemplo: python2 cliente_echo.py 0.0.0.0 5000')
    exit()

addr=sys.argv[1]
port=int(sys.argv[2])

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print ('conectando a %s puerto %d' % (addr, port))

cliente.connect((addr,port))


while True:
    mensaje = raw_input("Mensaje a enviar ")
    #print ('enviando "%s"' % (mensaje))
    cliente.sendall(mensaje)
    respuesta = cliente.recv(1024)
    print ('Recibido "%s"' % (respuesta))
    
    if mensaje.upper() == 'CERRAR':
        break
        print ('Cerrando la conexion')
        cliente.close()
