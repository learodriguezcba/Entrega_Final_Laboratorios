import socket
import sys

arglen=len(sys.argv)
if arglen<2:
    print('Ejemplo: python2 cliente_tag.py 5000')
    exit()

puerto=int(sys.argv[1])

ip = "0.0.0.0" 

servidor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

servidor.bind((ip, puerto))


print ("[*] Esperando conexiones en %s:%d" % (ip, puerto))

while True:
    dato, direccion = servidor.recvfrom(1024)
    print "[*] La conexion se ha establecido con %s:%d" % (direccion[0] , direccion[1])
    print "[*] El mensaje ha sido recibido: %s" % dato
    mensajes = open('mensajes.txt', 'a')	
    mensajes.write(dato+"\n")
    mensajes.close()
    