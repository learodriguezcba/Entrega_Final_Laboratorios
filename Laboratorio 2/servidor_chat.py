import socket
import sys
import select
import Queue

arglen=len(sys.argv)
if arglen<2:
    print('Ejemplo: python2 servidor_chat.py 5000')
    exit()

puerto=int(sys.argv[1])

timeout=60

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

cola_de_mensajes = {}
servidor.bind(("", puerto))
servidor.listen(1)

print ('Esperando para conectarse')

teclado=sys.stdin
salidas = [ ]
entradas=[teclado, servidor]
mensaje = ""
client_address=""
#s es un elemento de la  listo_leer
s=0

while True:
    listo_leer, listo_escribir, _err = select.select(entradas, [], [], timeout)
    
    if not listo_leer==[]:
        for s in listo_leer:
            
            if s is teclado:
                mensaje = teclado.readline()
                print ("> "+ mensaje)
                connection.sendall(mensaje)

            elif s is servidor:
                connection, client_address = s.accept()
                print ('Nueva conexion desde '+ str(client_address))
                connection.setblocking(0)
                entradas.append(connection)
                cola_de_mensajes[connection] = Queue.Queue()
        
            else:
                recibido = s.recv(4096)
                if str(recibido) == "cerrar\n":
                    print ("El cliente ha finalizado  el chat")
                    connection.sendall('Cerrando la conexion')
                    connection.close()
                    if s in salidas:
                        salidas.remove(s)
                        entradas.remove(s)
                        s.close()
                    break

                else: 
                    print ('Recibido ' + str(recibido) + ' de ' + str(s.getpeername()))
                    cola_de_mensajes[s].put(recibido)
                    if s not in salidas:
                        salidas.append(s)
    else:
        
        if client_address=="":
            print ('Cerrando conexion'+ client_address )
        else: 
            print ('Cerrando conexion')
        if s:
            if s in salidas:
                salidas.remove(s)
            if s in entradas:
                entradas.remove(s)
            s.close()
            del cola_de_mensajes[s]
            break
        else:
            break

    for s in listo_escribir:
        try:
            siguente_msj = cola_de_mensajes[s].get_nowait()
        except Queue.Empty:
            print ('Cola de salida para'+ s.getpeername() + 'esta vacia')
            salidas.remove(s)
        else:
            print ('Enviando'+ siguente_msj + 'a '+ s.getpeername())
            s.send(siguente_msj)