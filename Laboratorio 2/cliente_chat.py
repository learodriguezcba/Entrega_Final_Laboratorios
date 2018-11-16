import socket
import sys
import select

arglen=len(sys.argv)
if arglen<3:
    print('Ejemplo: python2 cliente_chat.py 0.0.0.0 5000')
    exit()

addr = sys.argv[1]
port = int(sys.argv[2])

timeout_in_seconds=60
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print ('conectando a %s puerto %d' % (addr, port))

nombre = raw_input("Ingresa tu nombre por favor ")

cliente.connect((addr,port))
cliente.sendall(nombre)
teclado=sys.stdin
entradas=[cliente, teclado]
flag=1

while flag==1:


    print (nombre + "> ")
    
    ready, _out, _err = select.select(entradas, [], [], timeout_in_seconds)
    
    for elem in ready:

        if elem == teclado:
            respuesta = teclado.readline()
            print ("> "+respuesta)
            cliente.sendall(respuesta)
            if str(respuesta) == "cerrar\n":
                cliente.close()
                print("Sesion finalizada")
                flag=0
                break
        elif elem == cliente:
            respuesta = cliente.recv(4096)
            print ("> "+respuesta)