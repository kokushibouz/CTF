import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.bind(('127.0.0.1', 10000))
	s.listen()
	conn, addr = s.accept()
	with conn:
		while True:
			data = conn.recv(1024)
			if not data:
				break
			print(data.decode())